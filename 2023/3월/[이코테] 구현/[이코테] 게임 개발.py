import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 행, 열, 방향
row, column, direction = map(int, input().split())

map = [list(map(int, input().split())) for i in range(N)]
answer = 1

# 방문 여부 체크 배열
visited = [[False for j in range(M)] for i in range(N)]
visited[row][column] = True

# 북, 서, 남, 동
move_row = [-1, 0, 1, 0]
move_column = [0, -1, 0, 1]


# 바다인 것은 방문 불가능하므로 이미 방문했다고 체크한다.
for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            visited[i][j] = True


while True:

    '''
    STEP 1 
    '''
    # 방향 반시계 방향 90도.
    direction = (direction + 1) % 4

    all_block = False
    block_cnt = 0

    nrow = row + move_row[direction]
    ncolumn = column + move_column[direction]

    # 동서남북 돌면서 사방이 막혀있는지 확인
    for i in range(4):
        nrow = row + move_row[(direction + i) % 4]
        ncolumn = column + move_column[(direction + i) % 4]

        if ncolumn < 0 or ncolumn >= M or nrow < 0 or nrow >= N:
            block_cnt += 1
            continue

        if map[nrow][ncolumn] == 1 or visited[nrow][ncolumn]:
            block_cnt += 1

    # 사방이 모두 막힌 경우 all_block 체크
    if block_cnt >= 4:
        all_block = True

    # step3 : 사방이 막혀있는 경우(가본곳 or 바다) 바라보고 있는 방향에서 뒤로 이동한다.
    if all_block:
        row = row - move_row[direction]
        column = column - move_column[direction]

        if column < 0 or column >= M or row < 0 or row >= N:
            break
        visited[row][column] = True

        # 이 때 뒤 칸이 바다였다면 멈추고 종료 (끝)
        if map[row][column] == 1:
            break

        # 육지라면 다시 시뮬레이션 진행
        continue

    '''
    STEP 2
    '''
    if map[nrow][ncolumn] == 0:
        if ncolumn < 0 or ncolumn >= M or nrow < 0 or nrow >= N:
            break

        if not visited[nrow][ncolumn]:
            row = nrow
            column = ncolumn
            answer += 1
            visited[nrow][ncolumn] = True

print(answer)
print(visited)
