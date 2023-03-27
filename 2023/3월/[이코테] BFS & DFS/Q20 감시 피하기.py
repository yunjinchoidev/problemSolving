import itertools
import copy
from pprint import pprint

N = int(input())

map_ = [list(map(str, input().split())) for i in range(N)]

coords = [(r, c) for c in range(N) for r in range(N) if map_[r][c] == 'X']
combis = list(itertools.combinations(coords, 3))

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def DFS(row, col, map_):
    visited = [[False for c in range(N)] for r in range(N)]
    stack = []
    stack.append((row, col))
    visited[row][col] = True

    while stack:
        r, c = stack.pop()

        for i in range(4):
            for dep in range(1, N + 1):

                nr = r + dr[i] * dep
                nc = c + dc[i] * dep

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                if map_[nr][nc] == 'O':
                    break

                if map_[nr][nc] == 'S':
                    # print("?", nr, nc)
                    # pprint(visited)
                    return False





                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    # stack.append((nr, nc))

    # pprint(visited)
    return True


# pprint(combis)
for comb in combis:
    copy_map_ = copy.deepcopy(map_)
    copy_map_[comb[0][0]][comb[0][1]] = 'O'
    copy_map_[comb[1][0]][comb[1][1]] = 'O'
    copy_map_[comb[2][0]][comb[2][1]] = 'O'

    answer = 'YES'

    # pprint(copy_map_)
    # print(comb)
    # if comb == ((1, 1), (0, 3), (3, 3)):
    for r in range(N):
        for c in range(N):
            if copy_map_[r][c] == 'T':
                if not DFS(r, c, copy_map_):
                    answer = 'NO'
        if answer == 'NO':
            break

    if answer == 'YES':
        break

print(answer)
