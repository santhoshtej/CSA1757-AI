import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(state):
    """Calculate the Manhattan distance heuristic."""
    distance = 0
    for i in range(9):
        if state[i] != 0:
            target_x, target_y = divmod(state[i] - 1, 3)
            current_x, current_y = divmod(i, 3)
            distance += abs(current_x - target_x) + abs(current_y - target_y)
    return distance

def get_neighbors(state):
    """Generate all valid neighbors (states) of the current state."""
    zero_index = state.index(0)
    x, y = divmod(zero_index, 3)
    neighbors = []
    
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx * 3 + ny
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))
    
    return neighbors

def a_star(start):
    """Solve the 8-puzzle using A* search algorithm."""
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start), 0, start, []))
    closed_set = set()
    closed_set.add(start)
    
    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        
        if state == GOAL:
            return path
        
        for neighbor in get_neighbors(state):
            if neighbor not in closed_set:
                closed_set.add(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(open_list, (g + 1 + manhattan_distance(neighbor), g + 1, neighbor, new_path))
    
    return None  

def print_puzzle(state):
    """Helper function to print the puzzle state in a 3x3 grid."""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def solve_puzzle(initial_state):
    """Solve the 8-puzzle problem given the initial state."""
    solution_path = a_star(initial_state)
    
    if solution_path:
        print("Solution found!")
        print("Steps to reach the goal:")
        for step in solution_path:
            print_puzzle(step)
    else:
        print("No solution found.")

# Example of solving the 8-puzzle problem
if __name__ == "__main__":

    initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    
    solve_puzzle(initial_state)
