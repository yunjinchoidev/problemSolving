from collections import deque

N, L, R = map(int, input().split())

contries = [list(map(int, input().split())) for i in range(N)]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def is_all_same(arr):
    total = 0
    count = 0
    for row in arr:
        for value in row:
            total += value
            count += 1
    avg = total / count

    for row in arr:
        for value in row:
            if value != avg:
                return False

    return True



def DFS(row, col, depth, sum_number, visited):
    stack = []
    stack.append((row, col, depth, sum_number))
    result = set()
    visited[row][col] = True
    is_updated = False

    while stack:
        r, c, d, sn = stack.pop()
        result.add((r, c))

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            human_gab = abs(contries[nr][nc] - contries[r][c])

            if not visited[nr][nc] and (L <= human_gab and human_gab <= R):
                stack.append((nr, nc, d + 1, sn + contries[nr][nc]))
                visited[nr][nc] = True
                result.add((nr, nc))


    if len(result) >= 2:
        is_updated = True

    s = 0
    for i, j in result:
        s += contries[i][j]

    for r in result:
        contries[r[0]][r[1]] = s // len(result)
    return is_updated


update_day = 0
while True:

    if is_all_same(contries):
        break

    visited = [[False for c in range(N)] for r in range(N)]

    is_update = True
    update_cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                is_update = DFS(r, c, 0, contries[r][c], visited)

                if is_update:
                    update_cnt += 1

    if update_cnt == 0:
        break
    update_day += 1
print(update_day)
