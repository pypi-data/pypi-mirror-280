import networkx as nx
import numpy as np
import random
from scipy import integrate, linalg
from typing import List
import warnings

from .functions.is_maximal_independent_set import is_maximal_independent_set

def blelloch(G: nx.Graph) -> List[int]:
    """
    Find a maximal independent set using Blelloch's parallel algorithm.

    Args:
        G (nx.Graph): An undirected graph.

    Returns:
        List[int]: A list of nodes representing a maximal independent set.
    """
    A = nx.to_numpy_array(G)  # Adjacency matrix of the graph
    n = len(A)
    in_mis = np.zeros(n, dtype=bool)  # Nodes in the maximal independent set
    excluded = np.zeros(n, dtype=bool)  # Nodes excluded from the MIS
    undecided = np.ones(n, dtype=bool)  # Nodes yet to be decided

    while np.any(undecided):
        # Randomly select candidates to potentially add to MIS
        candidates = (np.random.rand(n) < 0.5) & undecided
        
        for v in range(n):
            if candidates[v] and not excluded[v]:
                neighbors = np.where(A[v] == 1)[0]
                # Add vertex to MIS
                in_mis[v] = True
                # Exclude the vertex and its neighbors
                undecided[v] = False
                excluded[v] = True
                undecided[neighbors] = False
                excluded[neighbors] = True
        
        # Exclude all vertices that were decided in this iteration
        undecided[candidates & ~in_mis] = False

    output_indices = np.where(in_mis)[0]
    node_list = list(G.nodes())
    output_nodes = [node_list[i] for i in output_indices]
    
    if is_maximal_independent_set(G, output_nodes):
        return output_nodes

    else:
        print('Blelloch algorithm did not return MIS.')
        exit()