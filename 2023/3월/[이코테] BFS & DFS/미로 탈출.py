from pprint import pprint
from collections import deque

N, M = map(int, input().split())

map_ = []
for i in range(N):
    map_.append(list(map(int, str(input()))))

pprint(map_)

visited = [[False for c in range(M)] for r in range(N)]
pprint(visited)

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def DFS(row, col):
    stack = []
    stack.append((row, col, 0))
    visited[row][col] = True

    while stack:
        r, c, t = stack.pop()

        if r == N - 1 and c == M - 1:
            return t + 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if map_[nr][nc] == 1 and not visited[nr][nc]:
                stack.append((nr, nc, t + 1))
                visited[nr][nc] = True


def BFS(row, col):
    d = deque()
    d.append((row, col, 0))
    visited[row][col] = True

    while d:
        r, c, t = d.popleft()

        if r == N - 1 and c == M - 1:
            return t + 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if map_[nr][nc] == 1 and not visited[nr][nc]:
                d.append((nr, nc, t + 1))
                visited[nr][nc] = True


print(BFS(0, 0))
