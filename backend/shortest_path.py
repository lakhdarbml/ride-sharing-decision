import networkx as nx

def compute_shortest_path(G, orig_node, dest_node, weight="length"):
    """
    Calcule le plus court chemin dans le graphe.

    Args:
        G: Graphe OSMnx
        orig_node: ID du noeud de départ
        dest_node: ID du noeud d'arrivée
        weight: Critère d'optimisation ("length", "travel_time")

    Returns:
        list: séquence de noeuds représentant le chemin
    """
    return nx.shortest_path(G, orig_node, dest_node, weight=weight)
