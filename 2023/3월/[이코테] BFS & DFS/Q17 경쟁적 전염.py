from collections import deque

N, K = map(int, input().split())
map_ = [list(map(int, input().split())) for i in range(N)]
S, X, Y = map(int, input().split())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

orders = []

for r in range(N):
    for c in range(N):
        if map_[r][c] != 0:
            orders.append((r, c, 0, map_[r][c]))

orders = sorted(orders, key=lambda x: x[3])
orders = deque(orders)


def BFS(orders):
    global map_

    while orders:
        r, c, dep, num = orders.popleft()

        if dep == S:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if map_[nr][nc] == 0:
                map_[nr][nc] = num
                orders.append((nr, nc, dep + 1, num))


BFS(orders)
print(map_[X - 1][Y - 1])
