from collections import deque


def solution(maps):
    answer = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    d = deque()
    d.append((0, 0, 1))
    result = []

    visited = [[False for i in range(len(maps[0]))] for i in range(len(maps))]
    print(visited)

    while d:
        x, y, m = d.popleft()
        visited[x][y] = True

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            result.append(m)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1 and not visited[nx][ny]:
                print(nx, ny, m + 1)
                visited[nx][ny] = True
                d.append((nx, ny, m + 1))

    print(result)
    if len(result) >= 1:
        answer = min(result)
    else:
        answer = -1

    return answer
