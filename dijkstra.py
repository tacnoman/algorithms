graph = {
    'a': {'b': 3, 'c': 4, 'd': 7},
    'b': {'c': 1, 'f': 5},
    'c': {'f': 6, 'd': 2},
    'd': {'e': 3, 'g': 6},
    'e': {'g': 3, 'h': 4},
    'f': {'e': 1, 'h': 8},
    'g': {'h': 2},
    'h': {'g': 2},
}

inifinity = 99999999999999999999

def dijkstra(graph, start):
    unseen_nodes = graph
    shortest_distance = {}

    # set short distance for all nodes like infinity
    for index_node in unseen_nodes:
        shortest_distance[index_node] = inifinity

    shortest_distance[start] = 0

    while unseen_nodes:
        minimum_distance_index = None
        # find the minimum distance
        for index_node in unseen_nodes:
            if minimum_distance_index is None:
                minimum_distance_index = index_node
            elif shortest_distance[index_node] < shortest_distance[minimum_distance_index]:
                minimum_distance_index = index_node

        # Get items for graph with minimum distance
        path_options = graph[minimum_distance_index].items()

        # Add weight if is less to each node connected
        for child_node, weight in path_options:
            if weight + shortest_distance[minimum_distance_index] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[minimum_distance_index]

        # Remove because already calculated
        unseen_nodes.pop(minimum_distance_index)

    return shortest_distance


print(dijkstra(graph, 'a'))
