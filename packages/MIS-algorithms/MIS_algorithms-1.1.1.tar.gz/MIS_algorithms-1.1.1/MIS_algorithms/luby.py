import networkx as nx
import numpy as np
import random
from scipy import integrate, linalg
from typing import List, Set
import warnings

from .functions.is_maximal_independent_set import is_maximal_independent_set

def luby(G: nx.Graph) -> List[int]:
    """
    Find a maximal independent set using Luby's algorithm.

    Args:
        G (nx.Graph): An undirected graph.

    Returns:
        List[int]: A list of nodes representing a maximal independent set.
    """
    I: Set[int] = set()  # Independent set
    V: Set[int] = set(G.nodes)  # Set of all nodes in the graph
    
    while V:
        # Remove isolated vertices
        to_remove = [v for v in V if G.degree(v) == 0]
        I.update(to_remove)
        V -= set(to_remove)
        
        # Step 1: Choose a random set of vertices S
        S: Set[int] = {v for v in V if random.random() < 1 / (2 * G.degree(v))}
        
        # Step 2: Resolve conflicts in S
        to_remove = set()
        for u in S:
            for v in G.neighbors(u):
                if v in S:
                    if G.degree(u) < G.degree(v) or (G.degree(u) == G.degree(v) and u < v):
                        to_remove.add(u)
                    else:
                        to_remove.add(v)
        S -= to_remove
        
        # Step 3: Add S to I
        I.update(S)
        
        # Step 4: Remove S and all its neighbors from V
        neighbors = {n for v in S for n in G.neighbors(v)}
        V -= S | neighbors

    output = list(I)

    if is_maximal_independent_set(G, output):
        return output

    else:
        print('Luby algorithm did not return MIS.')
        exit()