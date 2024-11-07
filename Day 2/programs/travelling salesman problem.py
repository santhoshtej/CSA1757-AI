from itertools import permutations

# Function to calculate the total distance of a given route
def calculate_route_distance(route, distance_matrix):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to starting city
    return total_distance

# Function to find the shortest route using brute-force approach
def traveling_salesman_bruteforce(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    shortest_distance = float('inf')
    best_route = None

    # Generate all possible permutations of cities
    for route in permutations(cities):
        current_distance = calculate_route_distance(route, distance_matrix)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            best_route = route

    return best_route, shortest_distance

# Example distance matrix (symmetric matrix)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Find the best route
best_route, shortest_distance = traveling_salesman_bruteforce(distance_matrix)

# Print the result
print("Best route:", best_route)
print("Shortest distance:", shortest_distance)
