# 0 -> 빈칸
# 1 -> 벽
# 2 -> 바이러스
from pprint import pprint
import itertools
import copy
from collections import deque

N, M = map(int, input().split())
map_ = [list(map(int, input().split())) for row in range(N)]

coords = [(r, c) for c in range(M) for r in range(N) if map_[r][c] == 0]
result = list(itertools.combinations(coords, 3))

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# for r in range(N):
#     for c in range(M):
#         if map_[r][c] == 0:
#             visited[r][c] = True

max_zero = -float('inf')
for c in result:
    new_map = copy.deepcopy(map_)
    new_visited = visited = [[False for col in range(M)] for row in range(N)]
    new_map[c[0][0]][c[0][1]] = 1
    new_map[c[1][0]][c[1][1]] = 1
    new_map[c[2][0]][c[2][1]] = 1

    # print(new_map)


    def BFS(sr, sc):
        global new_map, new_visited

        d = deque()
        d.append((sr, sc))
        new_visited[sr][sc] = True

        while d:
            r, c = d.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue

                if new_map[nr][nc] == 0 and not new_visited[nr][nc]:
                    new_map[nr][nc] = 2
                    d.append((nr, nc))


    # pprint(new_map)
    # pprint(new_visited)
    for r in range(N):
        for c in range(M):
            if new_map[r][c] == 2 and not new_visited[r][c]:
                BFS(r, c)

    # pprint(new_map)
    # pprint(new_visited)
    c = 0

    for row in new_map:
        c += row.count(0)
    max_zero = max(c, max_zero)

print(max_zero)


#
#
#
# from itertools import combinations
# import copy
# from collections import deque
#
# N, M = map(int, input().split())
# map_ = [list(map(int, input().split())) for row in range(N)]
#
# coords = [(r, c) for c in range(M) for r in range(N) if map_[r][c] == 0]
# result = list(combinations(coords, 3))
#
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
# max_zero = -float('inf')
# for c in result:
#     new_map = copy.deepcopy(map_)
#     new_visited = [[False for col in range(M)] for row in range(N)]
#     new_map[c[0][0]][c[0][1]] = 1
#     new_map[c[1][0]][c[1][1]] = 1
#     new_map[c[2][0]][c[2][1]] = 1
#
#     def BFS(sr, sc):
#         global new_map, new_visited
#
#         d = deque()
#         d.append((sr, sc))
#         new_visited[sr][sc] = True
#
#         while d:
#             r, c = d.popleft()
#
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#
#                 if nr < 0 or nr >= N or nc < 0 or nc >= M:
#                     continue
#
#                 if new_map[nr][nc] == 0 and not new_visited[nr][nc]:
#                     new_map[nr][nc] = 2
#                     new_visited[nr][nc] = True
#                     d.append((nr, nc))
#
#     for r in range(N):
#         for c in range(M):
#             if new_map[r][c] == 2 and not new_visited[r][c]:
#                 BFS(r, c)
#
#     c = 0
#     for row in new_map:
#         c += row.count(0)
#     max_zero = max(c, max_zero)
#
# print(max_zero)
#
#
#
