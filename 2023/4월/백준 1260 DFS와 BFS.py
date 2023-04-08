from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

dfs_result = []
bfs_result = []


def dfs(graph, start):
    visited = [False for i in range(N + 1)]
    stack = []
    stack.append(start)

    while stack:
        n = stack.pop()

        if not visited[n]:
            dfs_result.append(n)
            visited[n] = True

            graph[n].sort(reverse=True)
            for i in graph[n]:
                if not visited[i]:
                    stack.append(i)

    return visited


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()

        graph[n].sort()
        if n not in visited:
            bfs_result.append(n)
            visited.append(n)
            for i in graph[n]:
                if i not in visited:
                    queue.append(i)
    return visited


dfs(graph, V)
bfs(graph, V)

print(*dfs_result)
print(*bfs_result)
# print(dfs_result)
# print(bfs_result)
