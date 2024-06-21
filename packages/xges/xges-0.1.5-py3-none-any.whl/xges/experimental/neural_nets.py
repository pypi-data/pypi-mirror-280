from collections import defaultdict

import torch
import torch.distributions as dist
import numpy as np
import tqdm

from xges.scorer import ScorerInterface


class DenseNN(torch.nn.Module):
    def __init__(self, n_inputs, hidden_layers, activation=torch.nn.ReLU()):
        super().__init__()
        self.layers = []
        self.activation = activation
        self.log_std = torch.nn.Parameter(torch.zeros(1))

        layer_sizes = [n_inputs] + list(hidden_layers) + [1]

        for n_in, n_out in zip(layer_sizes[:-1], layer_sizes[1:]):
            self.layers.append(torch.nn.Linear(n_in, n_out))
            self.layers.append(self.activation)
        self.layers = self.layers[:-1]
        self.model = torch.nn.Sequential(*self.layers)

    def forward(self, x):
        return self.model(x)[..., 0]

    def loss(self, x, y):
        """
        Compute the Gaussian loss of the model.
        """
        y_pred = self.forward(x)  # shape: n
        predicted_dist = dist.Normal(y_pred, torch.exp(self.log_std))
        return -predicted_dist.log_prob(y).sum()


class OneToOneNNParallel(torch.nn.Module):
    """
    Neural network that take a d-dimensional input, and returns a d x d-dimensional output.
    The output is a d*d matrix, where the i,j-th element is the score of having i as the only parent of j.
    """

    def __init__(self, n_inputs, hidden_layers, activation=torch.nn.ReLU()):
        super().__init__()
        self.activation = activation
        if len(hidden_layers) == 0:
            raise ValueError(
                "hidden_layers must have at least one element, use BIC score otherwise."
            )

        self.layer1_weight = torch.nn.Parameter(torch.randn(n_inputs, n_inputs, hidden_layers[0]))
        self.layer1_bias = torch.nn.Parameter(torch.randn(n_inputs, n_inputs, hidden_layers[0]))

        self.other_layer_weights = []
        self.other_layer_biases = []
        self.log_std = torch.nn.Parameter(torch.zeros(n_inputs, n_inputs))
        layer_sizes = list(hidden_layers) + [1]
        for n_in, n_out in zip(layer_sizes[:-1], layer_sizes[1:]):
            self.other_layer_weights.append(
                torch.nn.Parameter(torch.randn(n_inputs, n_inputs, n_in, n_out))
            )
            self.other_layer_biases.append(
                torch.nn.Parameter(torch.randn(n_inputs, n_inputs, n_out))
            )

    def forward(self, x):
        x = torch.einsum("ni,ijk->nijk", x, self.layer1_weight) + self.layer1_bias

        for w, b in zip(self.other_layer_weights, self.other_layer_biases):
            x = self.activation(x)
            x = torch.einsum("nijk,ijkl->nijl", x, w) + b

        return x[..., 0]

    def loss(self, x, y):
        """
        Compute the Gaussian loss of the model.
        """
        y_pred = self.forward(x)  # shape: n x d x d
        predicted_dist = dist.Normal(y_pred, torch.exp(self.log_std))
        return -predicted_dist.log_prob(y[:, None, :]).sum(dim=0)


def train(model, data_x, data_y, n_epochs=1000, lr=1e-3, batch_size=128, patience=10):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    data_loader = torch.utils.data.DataLoader(
        torch.utils.data.TensorDataset(data_x, data_y), batch_size=batch_size
    )
    pbar = tqdm.tqdm(range(n_epochs))

    best_loss = float("inf")
    patience_counter = 0

    for epoch in pbar:
        epoch_loss = 0
        for batch_x, batch_y in data_loader:
            optimizer.zero_grad()
            loss = model.loss(batch_x, batch_y).sum()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()

        if epoch_loss < best_loss:
            best_loss = epoch_loss
            patience_counter = 0
        else:
            patience_counter += 1

        if patience_counter >= patience:
            print("Early stopping due to no improvement in loss.")
            break

        pbar.set_description(f"Loss: {epoch_loss}")

    return model


def score_all_pairs(data, alpha=1.0, hidden_layers=(16,), lr=1e-3):
    """
    Return a matrix of all the diff scores for all pairs of variables.
    In [i,j] is the score of inserting i in the parents of j.
    Insert(i,j) = score(j, [i]) - score(j, [])
    """
    model = OneToOneNNParallel(data.shape[1], hidden_layers)
    model = train(model, data, data, lr=lr)
    bic = -model.loss(data, data).detach().numpy() - 0.5 * np.log(data.shape[0]) * alpha * 2
    return bic


def local_bic(data_target, data_parents, alpha=1.0, hidden_layers=(16,), lr=1e-3):
    model = DenseNN(data_parents.shape[1], hidden_layers)
    train(model, data_parents, data_target, lr=lr)
    n_parents = data_parents.shape[1]
    bic_regularization = 0.5 * np.log(data_target.shape[0]) * (n_parents + 1) * alpha
    bic = -model.loss(data_parents, data_target).detach().numpy() - bic_regularization
    return bic


class NeuralScorer(ScorerInterface):
    def __init__(self, data, alpha, hidden_layers=(16,), lr=1e-3):
        super().__init__()
        self.covariance = self.compute_covariance(data)
        self.data = torch.FloatTensor(data)
        self.alpha = alpha
        self.n_variables = data.shape[1]
        self.n_samples = data.shape[0]
        self.cache = [defaultdict(float) for _ in range(self.n_variables)]
        self.hidden_layers = hidden_layers
        self.lr = lr
        self.statistics = defaultdict(int)

        self.cache_score_all_pairs = None

    @staticmethod
    def compute_covariance(data):
        n_samples = data.shape[0]
        centered = data - np.mean(data, axis=0)
        covariance_matrix = np.dot(centered.T, centered) / n_samples
        return covariance_matrix

    def score_all_pairs(self):
        print("Computing all pairs")
        self.cache_score_all_pairs = score_all_pairs(
            self.data, self.alpha, self.hidden_layers, self.lr
        )
        # update cache
        for i in range(self.n_variables):
            for j in range(self.n_variables):
                self.cache[j][(i,)] = self.cache_score_all_pairs[i, j]
        return self.cache_score_all_pairs

    def local_score(self, target, parents):
        print(f"Computing local score from {parents} to {target}")
        self.statistics["local_score-#calls-total"] += 1
        parents = sorted(parents)
        cache_key = tuple(parents)
        if cache_key in self.cache[target]:
            return self.cache[target][cache_key]
        self.statistics["local_score-#calls-nocache"] += 1

        if len(parents) == 0:
            mean = self.data[:, target].mean()
            std = self.data[:, target].std()
            log_likelihood_no_constant = dist.Normal(mean, std).log_prob(self.data[:, target]).sum()
            bic_regularization = 0.5 * np.log(self.n_samples) * +1.0 * self.alpha
            bic = log_likelihood_no_constant - bic_regularization
        else:

            bic = local_bic(
                self.data[:, target],
                self.data[:, parents],
                self.alpha,
                self.hidden_layers,
                self.lr,
            )

        self.cache[target][cache_key] = bic

        return bic
