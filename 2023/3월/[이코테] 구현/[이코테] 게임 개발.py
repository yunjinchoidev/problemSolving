import sys

input = sys.stdin.readline

N, M = map(int, input().split())
row, column, direction = map(int, input().split())

map = [list(map(int, input().split())) for i in range(N)]
answer = 1
visited = [[False for j in range(M)] for i in range(N)]
visited[row][column] = True

# print(map)

# 북, 서, 남, 동 순
move_row = [-1, 0, 1, 0]
move_column = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            visited[i][j] = True

while True:
    # print(answer)
    # 방향 반시계 방향 90도.
    direction = (direction + 1) % 4

    all_block = False
    block_cnt = 0

    nrow = row + move_row[direction]
    ncolumn = column + move_column[direction]

    for i in range(4):
        nrow = row + move_row[(direction + i) % 4]
        ncolumn = column + move_column[(direction + i) % 4]

        if ncolumn < 0 or ncolumn >= M or nrow < 0 or nrow >= N:
            block_cnt += 1
            continue

        if map[nrow][ncolumn] == 1 or visited[nrow][ncolumn]:
            block_cnt += 1

    if block_cnt >= 4:
        all_block = True

    # 사방이 막혀있는 경우.
    if all_block:
        row = row - move_row[direction]
        column = column - move_column[direction]

        if column < 0 or column >= M or row < 0 or row >= N:
            break
        visited[row][column] = True


        if map[row][column] == 1:
            break

        continue

    if map[nrow][ncolumn] == 0:

        if ncolumn < 0 or ncolumn >= M or nrow < 0 or nrow >= N:
            break
        print(nrow, ncolumn, block_cnt, direction, answer, visited[nrow][ncolumn], "~~~~~~~~~~~~~~~~")

        if not visited[nrow][ncolumn]:

            row = nrow
            column = ncolumn
            answer += 1
            visited[nrow][ncolumn] = True

print(answer)
print(visited)
