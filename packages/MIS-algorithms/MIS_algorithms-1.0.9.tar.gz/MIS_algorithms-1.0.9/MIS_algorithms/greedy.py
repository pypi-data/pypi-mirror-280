import networkx as nx
import random
from .functions.is_maximal_independent_set import is_maximal_independent_set

def greedy(G: nx.Graph) -> list:
    """
    Find an independent set in a graph using the Greedy Minimal Degree algorithm.

    Parameters:
    - G (nx.Graph): The input graph.

    Returns:
    - list: List of nodes forming an independent set.
    """
    max_independent_set = []
    L = G.copy()

    while len(L.nodes()) != 0:
        # Find the node with the minimum degree in the current graph
        min_degree = min([L.degree(node) for node in L])
        nodes_with_min_degree = [node for node in L if L.degree(node) == min_degree]
        node_selected = random.choice(nodes_with_min_degree)

        # Add the selected node to the independent set
        max_independent_set.append(node_selected)

        # Remove the selected node and its neighbors from the current graph
        L.remove_nodes_from(G.neighbors(node_selected))
        L.remove_node(node_selected)

    if is_maximal_independent_set(G, max_independent_set):
        return max_independent_set
    else:
        print('Greedy algorithm did not return MIS.')
        exit()