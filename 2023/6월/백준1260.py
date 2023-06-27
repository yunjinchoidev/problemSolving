N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# print(graph)
for i in range(N + 1):
    graph[i].sort()

visited = [False for i in range(N+1)]

result = []

def dfs(s):
    global graph
    global result

    visited[s] = True
    result.append(s)
    for n in graph[s]:
        if not visited[n]:
            dfs(n)


dfs(V)

print(*result)


from collections import deque

bfs_result = []
visited = [False for i in range(N+1)]

def bfs(d):

    global bfs_result
    global graph

    while d:

        x = d.popleft()

        for n in graph[x]:
            if not visited[n]:
                d.append(n)
                bfs_result.append(n)
                visited[n] = True


d = deque()
d.append(V)
# print(bfs_result)
bfs_result.append(V)
visited[V]=True
bfs(d)
print(*bfs_result)