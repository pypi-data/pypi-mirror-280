import networkx as nx
import random

def barabasi_albert(size: int, m: int) -> nx.Graph:
    """
    Generates a Barabási-Albert (BA) scale-free network.
    
    Parameters:
    - size (int): The total number of nodes in the graph.
    - m (int): Number of edges to attach from a new node to existing nodes.
    
    Returns:
    - G (networkx.Graph): A NetworkX graph representing the BA model.
    """
    # Initialize the graph with m nodes
    G = nx.complete_graph(range(1, m+1))
    
    # List of existing nodes to target for new edges, with initial complete graph nodes
    target_nodes = list(range(1, m+1))

    for i in range(m+1, size+1):
        # Add a new node to the graph
        G.add_node(i)
        
        # Initialize a set to store target nodes for new edges
        targets = set()
        
        # Choose m unique target nodes for the new node
        while len(targets) < m:
            x = random.choice(target_nodes)
            targets.add(x)
        
        # Add edges from the new node to the chosen target nodes
        G.add_edges_from((i, target) for target in targets)
        
        # Update the list of target nodes
        target_nodes.append(i)
        target_nodes.extend(targets)
    
    return G