import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a dictionary to track the previous node in the shortest path.
    next_node = {node: None for node in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                next_node[neighbor] = current_node  # Update the previous node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = next_node[node]  # Trace back using the previous node

    if distances[end] != float('inf'):
        return distances[end], path
    else:
        return "No path exists from {} to {}".format(start, end)

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
end_node = 'D'

shortest_distance, path = dijkstra(graph, start_node, end_node)
print("Shortest Distance from {} to {}: {}".format(start_node, end_node, shortest_distance))
print("Shortest Path:", ' -> '.join(path))
