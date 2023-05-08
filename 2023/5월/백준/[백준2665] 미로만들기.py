from collections import deque

N = int(input())
map_ = [list(map(int, input())) for i in range(N)]

visited = [[False for c in range(N)] for r in range(N)]

d = deque()
d.append((0, 0, 0))
visited[0][0] = True

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

flip_cnt = 0

answer = 0
while d:
    r, c, f = d.popleft()

    # print(r, c, f)

    if r == N - 1 and c == N - 1:
        answer = f
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        # 흰색
        if map_[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            d.appendleft((nr, nc, f))

        elif map_[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True
            d.append((nr, nc, f + 1))

print(answer)
