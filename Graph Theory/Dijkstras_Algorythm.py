import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent_nodes = {}  # Dictionary to store neighboring nodes and their edge weights
        self.distance = float('inf')  # Distance from the start node
        self.visited = False  # Flag to track whether the node has been visited
        self.previous_node = None  # Previous node in the shortest path

    def add_neighbor(self, neighbor, weight):
        self.adjacent_nodes[neighbor] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def dijkstra(self, start_node_name):
        start_node = self.nodes[start_node_name]
        start_node.distance = 0

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node.visited:
                continue

            current_node.visited = True

            for neighbor, edge_weight in current_node.adjacent_nodes.items():
                distance = current_distance + edge_weight

                if distance < neighbor.distance:
                    neighbor.distance = distance
                    neighbor.previous_node = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

def reconstruct_path(end_node):
    path = []
    current_node = end_node

    while current_node is not None:
        path.insert(0, current_node.name)
        current_node = current_node.previous_node

    return path

# Example usage
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")

node_A.add_neighbor(node_B, 4)
node_A.add_neighbor(node_C, 2)
node_B.add_neighbor(node_D, 5)
node_C.add_neighbor(node_B, 1)
node_C.add_neighbor(node_D, 8)
node_D.add_neighbor(node_E, 3)
node_E.add_neighbor(node_A, 7)

graph = Graph()
graph.add_node(node_A)
graph.add_node(node_B)
graph.add_node(node_C)
graph.add_node(node_D)
graph.add_node(node_E)

start_node_name = "A"
graph.dijkstra(start_node_name)

end_node_name = "E"
end_node = graph.nodes[end_node_name]
shortest_path = reconstruct_path(end_node)
print("Shortest path:", shortest_path)
print("Shortest distance:", end_node.distance)
