from collections import deque

def bfs(graph, start_node):

    visited = set()
    queue = deque([start_node])

    visited.add(start_node)

    while queue:
 
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print("BFS starting from node 0:")
bfs(graph, 0)
