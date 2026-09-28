from collections import deque
#bfs
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

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return result

print("BFS Traversal:", bfs(graph, 'A'))

# dfs 
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

def dfs(graph, start):
    visited = set([start])
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        result.append(node)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return result

print("DFS Traversal:", dfs(graph, 'A'))




# Algorithm:
# BFS Algorithm:
# 1. Mark the starting node as visited and insert it into a queue.
# 2. While the queue is not empty, remove the front node and add it to the traversal result.
# 3. For each unvisited neighbour of that node, mark it visited and push it into the queue.
# DFS Algorithm:
# 1. Mark the starting node as visited and push it onto a stack.
# 2. While the stack is not empty, pop the top node and add it to the traversal result.
# 3. For each unvisited neighbour of that node, mark it visited and push it onto the stack.
# Explanation:
# BFS (Breadth-First Search) explores a graph level by level using a queue, visiting all neighbours of a node before moving deeper. DFS (Depth-First Search) explores as far as possible along each branch using a stack, then backtracks.
