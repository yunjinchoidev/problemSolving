from collections import deque
from pprint import pprint
import copy

N = int(input())
map_ = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

area_cnt = 1


def bfs(r, c):
    global area_cnt

    d = deque()
    d.append((r, c))
    while d:
        r, c = d.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and map_[nr][nc] == 1:
                    visited[nr][nc] = True
                    map_[nr][nc] = area_cnt
                    d.append((nr, nc))


for i in range(N):
    for j in range(N):
        if map_[i][j] == 1 and not visited[i][j]:
            map_[i][j] = area_cnt
            bfs(i, j)
            area_cnt += 1

# pprint(map_)

result = []


def bfs2(row, col, depth):
    d = deque()
    d.append((row, col, depth))

    global map__

    while d:
        r, c, d = d.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if (
                    not visited[nr][nc]
                    and map__[r][c] != 0
                    and map__[r][c] != map__[row][col]
                ):  # 그지점이 최솟값이요.
                    return d

                if not visited[nr][nc] and map_[nr][nc] == 0:  # 그 방향으론 일단 가시오.
                    visited[nr][nc] = True
                    map__[nr][nc] = d + 1
                    d.append((nr, nc, d + 1))


#
# for i in range(N):
#     for j in range(N):
#         visited = [[0] * N for _ in range(N)]
#         map__ = copy.deepcopy(map_)
#         if map__[i][j] != 0 and not visited[i][j]:
#             my_min = bfs2(i, j, 0)
#             result.append(my_min)
#
#         pprint(map__)
# print(result)
# print(min(result))

answer = float("inf")


# 바다를 건너며 가장 짧은 거리를 구한다.
def bfs2(z):
    global answer
    dist = [[-1] * N for _ in range(N)]  # 거리가 저장될 배열
    q = deque()

    for i in range(N):
        for j in range(N):
            if map_[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 갈 수 없는 곳이면 continue
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if map_[nr][nc] > 0 and map_[nr][nc] != z:
                answer = min(answer, dist[r][c])
                return
            # 바다를 만나면 dist를 1씩 늘린다.
            if map_[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append([nr, nc])


for i in range(1, area_cnt):
    bfs2(i)

print(answer)
