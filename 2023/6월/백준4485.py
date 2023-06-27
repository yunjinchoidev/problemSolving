import heapq

test = 0
while True:
    test += 1
    N = int(input())
    if N == 0:
        break

    map_ = [list(map(int, input().split())) for i in range(N)]

    s, e = 0, 0

    inference = [[int(1e9) for i in range(N)] for j in range(N)]
    visited = [[False for i in range(N)] for j in range(N)]
    inference[0][0] = 0
    visited[0][0] = True
    h = []
    heapq.heappush(h, (map_[0][0], 0, 0))
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while h:

        cost, r, c = heapq.heappop(h)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if cost > inference[nr][nc]:
                continue

            if not visited[nr][nc]:
                distance = cost + map_[nr][nc]
                if distance < inference[nr][nc]:
                    heapq.heappush(h, (distance, nr, nc))
                    inference[nr][nc] = distance
                    visited[nr][nc] = True

    print(f"Problem {test}: {inference[N-1][N-1]}")
