import networkx as nx
import pandas as pd
from netbone.backbone import Backbone
from netbone.filters import boolean_filter


# algo: h_backbone
# calculating H-Index

def h_backbone(data):
    if isinstance(data, pd.DataFrame):
        G = nx.from_pandas_edgelist(data, edge_attr='weight', create_using=nx.Graph())
    elif isinstance(data, nx.Graph):
        G = data.copy()
    else:
        print("data should be a panads dataframe or nx graph")
        return

    betweenness_values = nx.edge_betweenness_centrality(
        G, weight='weight', normalized=False)

    nx.set_edge_attributes(G, {edge: {'h_bridge': round(
        betweenness_values[edge] / len(G.nodes()), 3)} for edge in betweenness_values})
    #     for u, v in G.edges():
    #         G[u][v]['bridge'] = round(betweenness_values[(u,v)]/len(G.nodes()),3)

    weight_values = list(nx.get_edge_attributes(G, 'weight').values())
    bridge_values = list(nx.get_edge_attributes(G, 'h_bridge').values())

    # sorting in ascending order
    weight_values.sort()
    bridge_values.sort()

    h_weight = 0
    h_bridge = 0

    # iterating over the list
    for i, cited in enumerate(weight_values):

        # finding current result
        h_weight = len(weight_values) - i

        # if result is less than or equal
        # to cited then return result
        if h_weight <= cited:
            break

    # iterating over the list
    for i, cited in enumerate(bridge_values):

        # finding current result
        h_bridge = len(bridge_values) - i

        # if result is less than or equal
        # to cited then return result
        if h_bridge <= cited:
            break

    for u, v in G.edges():
        if G[u][v]['h_bridge'] >= h_bridge or G[u][v]['weight'] >= h_weight:
            G[u][v]['in_backbone'] = True
        else:
            G[u][v]['in_backbone'] = False

    return Backbone(nx.to_pandas_edgelist(G), method_name="H-Backbone Filter", property_name="h_bridge",
                    ascending=False, compatible_filters=[boolean_filter], filter_on='Edges')
