"""
This file contains all the functions used in the notebooks 
under the Binary Quadratic Model section.
"""
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx


# Task 3
linear = {"x1": 3, "x2": -1, "x3": 10, "x4": 7}
quadratic = {("x1", "x2"): 2, ("x1", "x3"): -5, ("x2", "x3"): 3, ("x3", "x4"): 11}
offset = 8
vartype = "BINARY"


def graph_viz(G):
    """Visualize NetworkX graph.

    Parameters
    ----------
    G : networkx.Graph
        The NetworkX graph to be visualized.
    """
    nx.draw_kamada_kawai(
        G,
        with_labels=True,
        node_size=700,
        width=3,
        font_size=14,
        font_weight="bold",
        font_color="whitesmoke",
    )
    plt.axis("off")
    plt.show()


def maxcut_viz(G, cut_nodes):
    """Visualize the output of MaxCut problem.

    Parameters
    ----------
    G : networkx.Graph
        Problem NetworkX graph.
    cut_nodes : dict

    """
    if isinstance(cut_nodes, dict):
        cut = set()
        for node, value in cut_nodes.items():
            if value == 1:
                cut.add(node)
    else:
        cut = cut_nodes

    S0 = [node for node in G.nodes if node in cut]
    S1 = [node for node in G.nodes if node not in cut]

    cut_edges = [
        (u, v)
        for u, v in G.edges
        if (u in S0 and v not in S0) or (u in S1 and v not in S1)
    ]
    uncut_edges = [
        (u, v) for u, v in G.edges if (u in S0 and v in S0) or (u in S1 and v in S1)
    ]

    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=S0, node_color="tab:red", node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=S1, node_color="tab:green", node_size=700)
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=cut_edges,
        style="dashed",
        edge_color="tab:blue",
        alpha=0.7,
        width=3,
    )
    nx.draw_networkx_edges(G, pos, edgelist=uncut_edges, style="solid", width=3)
    nx.draw_networkx_labels(
        G, pos, font_size=14, font_weight="bold", font_color="whitesmoke"
    )

    plt.tight_layout()
    plt.axis("off")
    plt.show()


def graph_coloring_viz(G, coloring):
    """Visualize the output of graph coloring problem.

    Parameters
    ----------
    G : networkx.Graph
        Problem NetworkX graph.

    coloring : dict
        The colors assigned to the nodes.
    """
    colors = list(mcolors.TABLEAU_COLORS)

    pos = nx.kamada_kawai_layout(G)

    for node, color in coloring.items():
        if isinstance(color, int):
            nx.draw_networkx_nodes(
                G, pos, nodelist=[node], node_color=[colors[color]], node_size=700
            )
        elif isinstance(color, list):
            nx.draw_networkx_nodes(
                G, pos, nodelist=[node], node_color=[colors[color[0]]], node_size=700
            )

    nx.draw_networkx_edges(G, pos, edgelist=G.edges, style="solid", width=3)
    nx.draw_networkx_labels(
        G, pos, font_size=14, font_weight="bold", font_color="whitesmoke"
    )
    plt.tight_layout()
    plt.axis("off")
    plt.show()
