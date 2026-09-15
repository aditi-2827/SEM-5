import heapq

h = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3,
    'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
}

graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('D', 2), ('C', 3)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('G', 3), ('H', 2), ('E', 5), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

def a_star(start, goal):
    open_list = [(h[start], 0, start)]
    g_score = {start: 0}
    parent = {}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:
            path = [current]

            while current in parent:
                current = parent[current]
                path.append(current)

            path.reverse()
            return path, g

        for neighbour, cost in graph[current]:
            new_g = g + cost

            if neighbour not in g_score or new_g < g_score[neighbour]:
                g_score[neighbour] = new_g
                parent[neighbour] = current

                f = new_g + h[neighbour]
                heapq.heappush(open_list, (f, new_g, neighbour))

    return None, None


path, cost = a_star('A', 'J')

print("A* Path:", path)
print("Total Cost:", cost)

