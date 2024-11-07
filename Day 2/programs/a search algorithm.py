from queue import PriorityQueue

# A* search function
def a_star_search(graph, start, goal, heuristic):
    # Priority queue to store (cost, node) pairs
    open_set = PriorityQueue()
    open_set.put((0, start))

    # Dictionary to store the cost to reach each node
    g_cost = {start: 0}

    # Dictionary to store the path
    came_from = {start: None}

    while not open_set.empty():
        # Get the node with the lowest estimated cost
        current_cost, current_node = open_set.get()

        # If we reach the goal, reconstruct and return the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], g_cost[goal]  # Return reversed path and total cost

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            new_cost = g_cost[current_node] + weight

            # If a new shortest path to neighbor is found
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                open_set.put((f_cost, neighbor))
                came_from[neighbor] = current_node

    # If the goal is not reachable, return None
    return None, float('inf')

# Example graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Example heuristic (straight-line distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0  # Goal node
}

# Define start and goal nodes
start = 'A'
goal = 'E'

# Run A* search
path, cost = a_star_search(graph, start, goal, heuristic)

# Print results
print("Path:", path)
print("Total cost:", cost)
