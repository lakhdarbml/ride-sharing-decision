import osmnx as ox

def load_graph(place_name: str, network_type: str = "drive"):
    """
    Charger un graphe routier depuis OpenStreetMap avec OSMnx.
    
    Args:
        place_name (str): Nom de la ville ou zone.
        network_type (str): Type de réseau ("drive", "walk", etc.)
    
    Returns:
        networkx.MultiDiGraph
    """
    G = ox.graph_from_place(place_name, network_type=network_type)
    # Sauvegarder en format GraphML
    ox.save_graphml(G, filepath="bordj_el_bahri.graphml")
    return G
