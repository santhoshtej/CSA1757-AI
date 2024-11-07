# Define the map (neighbors of each state)
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []  # Tasmania has no neighbors
}

# Define possible colors
colors = ["Red", "Green", "Blue"]

# Function to check if the color assignment is valid
def is_valid(state, color, assignment, neighbors):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function to find color assignment
def backtrack(assignment, neighbors, colors):
    # Check if assignment is complete
    if len(assignment) == len(neighbors):
        return assignment

    # Get the next state to assign
    unassigned_states = [state for state in neighbors if state not in assignment]
    state = unassigned_states[0]  # Use the first unassigned state

    for color in colors:
        # Check if assigning this color is valid
        if is_valid(state, color, assignment, neighbors):
            # Make the assignment
            assignment[state] = color
            # Recursively call backtracking
            result = backtrack(assignment, neighbors, colors)
            if result:
                return result
            # If failed, undo assignment
            del assignment[state]

    return None

# Solve the map coloring problem
def map_coloring(neighbors, colors):
    assignment = {}
    return backtrack(assignment, neighbors, colors)

# Run the map coloring function
result = map_coloring(neighbors, colors)

# Print the result
print("Color assignment for each state:")
if result:
    for state, color in result.items():
        print(f"{state}: {color}")
else:
    print("No solution found.")
  
