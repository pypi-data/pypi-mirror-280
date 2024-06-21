import sdcd.utils.train_utils
import torch
from sdcd.simulated_data import random_model_gaussian_global_variance
import numpy as np

torch.manual_seed(0)
np.random.seed(0)


def generate_data(n, d, n_edges):
    np.random.seed(0)
    true_causal_model = random_model_gaussian_global_variance(
        d,
        n_edges,
        scale=0.5,
    )
    B_true = true_causal_model.adjacency
    X_df = true_causal_model.generate_dataframe_from_all_distributions(
        n_samples_control=n, n_samples_per_intervention=0, subset_interventions=[]
    )
    X_df.iloc[:, :-1] = (X_df.iloc[:, :-1] - X_df.iloc[:, :-1].mean()) / X_df.iloc[
        :, :-1
    ].std()  # Normalize the data
    return X_df, B_true


data, true_graph = generate_data(10000, 5, 5)
print(data.values[-1, -2])

# %%
from xges import XGES
from xges.experimental import neural_nets, trees
import torch

# setup logging
xges_model = XGES()
x = data[data.columns[:-1]].values
xges_model.fit(
    x.astype(np.float64),
    False,
    # scorer=neural_nets.NeuralScorer(x, 2, (16,), lr=1e-3),
    scorer=trees.BICScorerNGBoost(x, 5),
    verbose=3,
)

# %%
# get the learned graph
learned_adjacency = xges_model.get_a_dag().to_adjacency_matrix()

import sdcd

res_xges = sdcd.utils.train_utils.compute_metrics(learned_adjacency, true_graph)
print(res_xges["shd"])

# %%
xges_model.total_score
