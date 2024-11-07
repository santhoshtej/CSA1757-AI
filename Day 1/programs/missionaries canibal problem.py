from collections import deque

def is_safe(m_left, c_left, m_right, c_right):
    return (m_left >= c_left or m_left == 0) and (m_right >= c_right or m_right == 0)

def possible_moves(m_left, c_left, boat_position):
    moves = []
    if boat_position == 0:  
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2 and m <= m_left and c <= c_left:
                    new_m_left, new_c_left = m_left - m, c_left - c
                    new_m_right, new_c_right = 3 - new_m_left, 3 - new_c_left
                    if is_safe(new_m_left, new_c_left, new_m_right, new_c_right):
                        moves.append((new_m_left, new_c_left, 1))
    else:
        
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2 and m <= 3 - m_left and c <= 3 - c_left:
                    new_m_left, new_c_left = m_left + m, c_left + c
                    new_m_right, new_c_right = 3 - new_m_left, 3 - new_c_left
                    if is_safe(new_m_left, new_c_left, new_m_right, new_c_right):
                        moves.append((new_m_left, new_c_left, 0))
    return moves

def solve():
    initial = (3, 3, 0)
    goal = (0, 0, 1)
    queue = deque([(initial, [])])
    visited = {initial}

    while queue:
        (m_left, c_left, boat_position), path = queue.popleft()
        if (m_left, c_left, boat_position) == goal:
            return path + [(m_left, c_left, boat_position)]

        for next_state in possible_moves(m_left, c_left, boat_position):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(m_left, c_left, boat_position)]))
    return None

solution = solve()

if solution:
    for state in solution:
        print(f"Missionaries on left: {state[0]}, Cannibals on left: {state[1]}, Boat on {'left' if state[2] == 0 else 'right'}")
else:
    print("No solution found.")
