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
    G = nx.complete_graph(range(1, m+2))
    
    # List of existing nodes to target for new edges, with initial complete graph nodes
    target_nodes = list(range(1, m+2))

    for i in range(m+2, size+1):
        # Add a new node to the graph
        G.add_node(i)
        
        # Calculate the probability of connecting to existing nodes based on their degree
        degrees = [G.degree(node) for node in target_nodes]
        total_degree = sum(degrees)
        probabilities = [degree / total_degree for degree in degrees]
        
        # Choose m unique target nodes for the new node, based on the calculated probabilities
        targets = set()
        while len(targets) < m:
            target = random.choices(target_nodes, weights=probabilities, k=1)[0]
            targets.add(target)
        
        # Add edges from the new node to the chosen target nodes
        G.add_edges_from((i, target) for target in targets)
        
        # Update the list of target nodes
        target_nodes.append(i)
        target_nodes.extend(targets)
    
    return G