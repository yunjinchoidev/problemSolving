import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))

graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


answer = 0

for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if graph[i][j] != int(1e9) or graph[j][i] != int(1e9):
            count += 1
    if count == N:
        answer += 1

print(answer)