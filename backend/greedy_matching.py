import osmnx as ox
import networkx as nx
from shortest_path import compute_shortest_path
from graph_loader import load_graph
def calculate_route_length(G, path):
    """Compute total length of a path in meters."""
    return sum(ox.utils_graph.get_route_edge_attributes(G, path, "length"))

def evaluate_match(G, driver, passenger):
    """
    Compute extra distance if driver picks up passenger.
    Returns detour in meters.
    """
    orig_node = ox.distance.nearest_nodes(G, driver["origin"][1], driver["origin"][0])
    dest_node = ox.distance.nearest_nodes(G, driver["destination"][1], driver["destination"][0])
    base_path = compute_shortest_path(G, orig_node, dest_node)
    base_dist = calculate_route_length(G, base_path)

    # Passenger pickup and dropoff
    p_orig = ox.distance.nearest_nodes(G, passenger["origin"][1], passenger["origin"][0])
    p_dest = ox.distance.nearest_nodes(G, passenger["destination"][1], passenger["destination"][0])

    # Driver route with passenger
    path_with_p = (
        compute_shortest_path(G, orig_node, p_orig) +
        compute_shortest_path(G, p_orig, p_dest)[1:] +
        compute_shortest_path(G, p_dest, dest_node)[1:]
    )
    new_dist = calculate_route_length(G, path_with_p)

    detour = new_dist - base_dist
    return detour, path_with_p

def match_passengers(G, drivers, passengers, detour_threshold=2000):
    """
    Match passengers to drivers if detour is acceptable.
    """
    matches = {}
    for driver in drivers:
        assigned = []
        for passenger in passengers:
            detour, path_with_p = evaluate_match(G, driver, passenger)
            if detour < detour_threshold and len(assigned) < driver["capacity"]:
                assigned.append({"passenger": passenger["id"], "detour": detour})
        matches[driver["id"]] = assigned
    return matches


def main():
    G = load_graph("Algiers, Algeria")

    drivers = [
        {"id": "D1", "origin": (36.75, 3.06), "destination": (36.78, 3.05), "capacity": 2},
    ]
    passengers = [
        {"id": "P1", "origin": (36.76, 3.07), "destination": (36.79, 3.05)},
    ]

    result = match_passengers(G, drivers, passengers)
    print(result)

if __name__ == "__main__":
    main()
