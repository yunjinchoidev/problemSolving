import sys
from collections import deque
from pprint import pprint


def input():
    return sys.stdin.readline().rstrip()

T = int(input())


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(row, col, visited):
    global cabbage

    global N
    global M
    global K

    d = deque()
    d.append((row, col))
    visited[row][col] = True

    while d:
        r, c = d.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N  or nc < 0 or nc >= M:
                continue

            if cabbage[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                d.append((nr, nc))


# N행 M열
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        cabbage[r][c] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]

    answer = 0
    for r in range(N):
        for c in range(M):
            if cabbage[r][c] == 1 and not visited[r][c]:
                bfs(r, c, visited)
                answer += 1

    print(answer)

