import ngboost
import ngboost.distns

from collections import defaultdict

import numba as nb
import numpy as np
from scipy.special import gammaln
from sklearn.model_selection import train_test_split

from xges.scorer import ScorerInterface

from xgboost_distribution import XGBDistribution


class BICScorerNGBoost(ScorerInterface):
    def __init__(self, data, alpha):
        super().__init__()
        self.data = data
        self.alpha = alpha
        self.covariance_matrix = self.compute_covariance(data)
        self.n_variables = data.shape[1]
        self.n_samples = data.shape[0]
        self.cache = [defaultdict(float) for _ in range(self.n_variables)]
        self.statistics = defaultdict(int)

        self.cache_score_all_pairs = None

    @staticmethod
    def compute_covariance(data):
        n_samples = data.shape[0]
        centered = data - np.mean(data, axis=0)
        covariance_matrix = np.dot(centered.T, centered) / n_samples
        return covariance_matrix

    def local_score(self, target, parents):
        self.statistics["local_score-#calls-total"] += 1
        parents = sorted(parents)
        cache_key = tuple(parents)
        if cache_key in self.cache[target]:
            return self.cache[target][cache_key]
        self.statistics["local_score-#calls-nocache"] += 1

        if len(parents) == 0:
            mean = self.data[:, target].mean()
            std = self.data[:, target].std()

        else:
            X = self.data[:, parents]
            y = self.data[:, [target]]
            # model = ngboost.NGBRegressor(early_stopping_rounds=50)
            # model.fit(X, y)
            # distribution = model.pred_dist(X)
            # log_likelihood = distribution.logpdf(y.squeeze(-1)).sum()
            X_train, X_test, y_train, y_test = train_test_split(X, y)

            model = XGBDistribution(
                distribution="normal",
                n_estimators=500,
                early_stopping_rounds=10,
            )
            model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
            preds = model.predict(X)
            mean, std = preds.loc, preds.scale

        from scipy.stats import norm

        log_likelihood = norm(mean, std).logpdf(self.data[:, target]).sum()

        bic = log_likelihood - 0.5 * len(parents) * np.log(self.n_samples) * self.alpha
        print(target, parents, log_likelihood)

        self.cache[target][cache_key] = bic

        return bic
