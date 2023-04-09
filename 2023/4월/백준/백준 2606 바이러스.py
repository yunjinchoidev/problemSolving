N = int(input())
M = int(input())

adjacent = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

visited = [False for i in range(N+1)]

def dfs(v):
    visited[v] = True
    for i in adjacent[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(visited.count(True)-1)

