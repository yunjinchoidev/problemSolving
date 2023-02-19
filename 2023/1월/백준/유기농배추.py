from collections import deque


def BFS(graph, w, h, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    d = deque()
    d.append((w, h))
    visited[w][h] = True

    while d:
        a, b = d.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= len(visited) or ny >= len(visited[0]):
                continue

            if not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                d.append((nx, ny))
    return 1


T = int(input())

for i in range(T):
    cnt = 0
    M, N, K = map(int, input().split(" "))
    m = [[0 for p in range(M)] for q in range(N)]
    visited = [[False for p in range(M)] for q in range(N)]
    for u in range(K):
        x, y = map(int, input().split(" "))
        m[y][x] = 1

    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] == False and m[i][j] != 0:
                cnt += BFS(m, i, j, visited[:])

    print(cnt)
