from scipy.stats import binom
import pandas as pd
import networkx as nx
from netbone.backbone import Backbone
from netbone.filters import threshold_filter, fraction_filter

# algo: noise_corrected.py
def noise_corrected(data, approximation=True):

    if isinstance(data, pd.DataFrame):
        g = nx.from_pandas_edgelist(data, edge_attr='weight', create_using=nx.Graph())
    elif isinstance(data, nx.Graph):
        g = data.copy()
    else:
        print("data should be a panads dataframe or nx graph")
        return

    n = sum(nx.get_edge_attributes(g, name='weight').values())

    for i, j, w in g.edges(data='weight'):
        ni= g.degree(i, weight='weight')
        nj= g.degree(j, weight='weight')
        mean_prior_probability = ((ni * nj) / n) * (1 / n)
        kappa = n / (ni * nj)
        if approximation:
            g[i][j]['p_value'] = 1-binom.cdf(w, n, mean_prior_probability)
        else:
            score = ((kappa * w) - 1) / ((kappa * w) + 1)
            var_prior_probability = (1 / (n ** 2)) * (ni * nj * (n - ni) * (n - nj)) / ((n ** 2) * ((n - 1)))
            alpha_prior = (((mean_prior_probability ** 2) / var_prior_probability) * (1 - mean_prior_probability)) - mean_prior_probability
            beta_prior = (mean_prior_probability / var_prior_probability) * (1 - (mean_prior_probability ** 2)) - (1 - mean_prior_probability)

            alpha_post = alpha_prior + w
            beta_post = n - w + beta_prior
            expected_pij = alpha_post / (alpha_post + beta_post)
            variance_nij = expected_pij * (1 - expected_pij) * n
            d = (1.0 / (ni * nj)) - (n * ((ni + nj) / ((ni * nj) ** 2)))
            variance_cij = variance_nij * (((2 * (kappa + (w * d))) / (((kappa * w) + 1) ** 2)) ** 2)
            sdev_cij = variance_cij ** .5
            g[i][j]['nc_sdev'] = sdev_cij
            g[i][j]['score'] = score

    return Backbone(g, method_name="Noise Corrected Filter", property_name="p_value", ascending=True, compatible_filters=[threshold_filter, fraction_filter], filter_on='Edges')

