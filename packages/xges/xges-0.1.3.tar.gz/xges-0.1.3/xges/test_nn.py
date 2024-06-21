import sdcd.utils.train_utils
from sdcd.simulated_data import random_model_gaussian_global_variance


def generate_data(n, d, n_edges):
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


# %%
data, true_graph = generate_data(10000, 10, 10)

# %%
# run SDCD
from sdcd.models import SDCD
from sdcd.utils import create_intervention_dataset

X_dataset = create_intervention_dataset(data, perturbation_colname="perturbation_label")
model = SDCD(standard_scale=False)
model.train(X_dataset, finetune=False, verbose=True)

# %%
# get the learned graph
learned_adjacency = model.get_adjacency_matrix(threshold=True)

# %%
import sdcd

res_sdcd = sdcd.utils.train_utils.compute_metrics(learned_adjacency, true_graph)
print("SDCD", res_sdcd["shd"])


# %%
from xges import XGES
from xges.experimental import neural_nets


# %%
