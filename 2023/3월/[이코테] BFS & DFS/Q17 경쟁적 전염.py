# from collections import deque
#
# N, K = map(int, input().split())
# map_ = [list(map(int, input().split())) for i in range(N)]
# S, X, Y = map(int, input().split())
#
# # 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# orders = []
#
# for r in range(N):
#     for c in range(N):
#         if map_[r][c] != 0:
#             orders.append((r, c, 0, map_[r][c]))
#
# # 숫자 순으로 정렬
# orders = sorted(orders, key=lambda x: x[3])
# orders = deque(orders)
#
#
# # 적은 초, 작은 숫자 부터 증식하므로 규칙을 만족하게 된다.
# def BFS(orders):
#     global map_
#
#     while orders:
#         r, c, dep, num = orders.popleft()
#
#         # S 시간 까지 퍼지고 다음엔 진행이 안되어야 하므로 S 에서 멈춘다.
#         if dep == S :
#             break
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                 continue
#
#             if map_[nr][nc] == 0:
#                 map_[nr][nc] = num  # BFS 로직에 따라 우선순위 바이러스가 공간을 먼저 차지함.
#                 orders.append((nr, nc, dep + 1, num))
#
#
# BFS(orders)
#
# print(map_[X - 1][Y - 1])  # S 초후 (X,Y) 에 존재하는 바이러스


from collections import deque
import copy
import heapq
from pprint import pprint

N, M = map(int, input().split())
map_ = [list(map(int, input().split())) for i in range(N)]
S, X, Y = map(int, input().split())

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visited = [[False for c in range(N)] for r in range(N)]

# 모든 바이러스 시점을 출발점으로 S 초가 진행되었다고 했을 때 만들어지는 누적 합 배열
prefix_sum_map = [[[] for c in range(N)] for r in range(N)]

for r in range(N):
    for c in range(N):
        if map_[r][c] != 0:
            heapq.heappush(prefix_sum_map[r][c], [0, map_[r][c]])


def BFS(row, col, depth, number):
    d = deque()
    d.append((row, col, depth, number))
    visited = [[False for c in range(N)] for r in range(N)]
    visited[row][col] = True

    # 최초에 바이러스가 있는 지점은 못 감.
    for r in range(N):
        for c in range(N):
            if map_[r][c] != 0:
                visited[r][c] = True

    while d:
        r, c, dep, num = d.popleft()

        # S 시간 까지 퍼지고 다음엔 진행이 안되어야 하므로 S 에서 멈춘다.
        if dep == S:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if not visited[nr][nc]:
                visited[nr][nc] = True
                prefix_sum_map[nr][nc].append([dep + 1, num])
                d.append((nr, nc, dep + 1, num))


for r in range(N):
    for c in range(N):
        if map_[r][c] != 0:
            BFS(r, c, 0, map_[r][c])

answer = 0

heapq.heapify(prefix_sum_map[X - 1][Y - 1])

if prefix_sum_map[X - 1][X - 1] == []:
    answer = 0
else:
    answer = prefix_sum_map[X - 1][Y - 1][0][1]

pprint(prefix_sum_map)
print(answer)
