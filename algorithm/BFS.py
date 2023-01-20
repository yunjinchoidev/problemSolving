# BFS

from collections import deque

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
def BFS(graph, root):
    visited = []
    q = deque([root])

    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            q += graph[n] - set(visited)
    return visited

print(BFS(graph_list, root_node))



