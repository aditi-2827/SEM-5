from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

# BFS (Breadth First Search)
def bfs(graph, start):
    visited = set()          # keeps track of visited nodes
    queue = deque()          # queue for BFS
    visited.add(start)       # mark start as visited
    queue.append(start)      # push start into queue
    result = []              # stores traversal order

    while queue:
        node = queue.popleft()      # remove front node
        result.append(node)         # add it to result
        for neighbour in graph[node]:       # check all neighbours
            if neighbour not in visited:    # if not visited
                visited.add(neighbour)      # mark visited
                queue.append(neighbour)     # add to queue
    return result
print("BFS Traversal:", bfs(graph, 'A'))

# DFS (Depth First Search)
def dfs(graph, start):
    visited = set()          # keeps track of visited nodes
    stack = [start]          # stack for DFS
    visited.add(start)       # mark start as visited
    result = []              # stores traversal order

    while stack:
        node = stack.pop()              # remove top node
        result.append(node)             # add it to result
        for neighbour in graph[node]:   # check all neighbours
            if neighbour not in visited:    # if not visited
                visited.add(neighbour)      # mark visited
                stack.append(neighbour)     # add to stack
    return result

print("DFS Traversal:", dfs(graph, 'A'))


