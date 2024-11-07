from collections import deque

def water_jug_problem(x, y, z):
    if z > max(x, y):
        return "Solution not possible"
    
    visited = set()
    
    queue = deque([(0, 0)]) 
    
    while queue:
        a, b = queue.popleft()
        
        if a == z or b == z:
            return f"Solution found: Jug1 = {a}, Jug2 = {b}"
        
        if (a, b) in visited:
            continue
        visited.add((a, b))

        possible_states = [
            (x, b), 
            (a, y), 
            (0, b), 
            (a, 0),  
            (a - min(a, y - b), b + min(a, y - b)),  
            (a + min(b, x - a), b - min(b, x - a))  
        ]
        
        for state in possible_states:
            if state not in visited:
                queue.append(state)
    
    return "Solution not possible"

# Example usage
x = 4 
y = 3  
z = 2 

print(water_jug_problem(x, y, z))
