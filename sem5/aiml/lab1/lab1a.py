import heapq
def tsp_a_star(start_node, adjacency_matrix, heuristic_values):
    num_nodes = len(adjacency_matrix)
    class Node:
        def __init__(self, current_path, path_cost=0):
            self.current_path = current_path
            self.path_cost = path_cost
            self.heuristic = self.calculate_heuristic()
        # Heuristic: Minimum distance to an unvisited node
        def calculate_heuristic(self):
            last_node = self.current_path[-1]
            unvisited = [node for node in range(num_nodes) if node not in self.current_path]
            if not unvisited:
                return adjacency_matrix[last_node][start_node]  # Return to start if all cities are visited
            return min(adjacency_matrix[last_node][node] for node in unvisited)
        def __lt__(self, other):
            return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)
    start = Node([start_node])
    priority_queue = [start]
    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        # If we've visited all cities and returned to the start, we found a solution
        if len(current_node.current_path) == num_nodes + 1 and current_node.current_path[-1] == start_node:
            return current_node.current_path
        last_visited = current_node.current_path[-1]
        for neighbour in range(num_nodes):
            if neighbour not in current_node.current_path:
                new_path = current_node.current_path + [neighbour]
                new_cost = current_node.path_cost + adjacency_matrix[last_visited][neighbour]
                heapq.heappush(priority_queue, Node(new_path, new_cost))
            elif len(current_node.current_path) == num_nodes and neighbour == start_node:
                new_path = current_node.current_path + [start_node]
                new_cost = current_node.path_cost + adjacency_matrix[last_visited][start_node]
                heapq.heappush(priority_queue, Node(new_path, new_cost))
    return []
start_node=0
adjacency_matrix=[
        [0,10,15,20],
        [10,0,35,25],
        [15,35,0,30],
        [20,25,30,0]
    ]
heuristic_values=[70,15,10,20]
path_modified = tsp_a_star(start_node, adjacency_matrix, heuristic_values)
print("TSP Path: ",path_modified)