# https://www.acmicpc.net/problem/3190
import sys
from pprint import pprint

input = sys.stdin.readline

N = int(input())
apple_cnt = int(input())

apples = []

for i in range(apple_cnt):
    apples.append(list(map(int, input().split())))

turn_cnt = int(input())
turns = []
for i in range(turn_cnt):
    turns.append(list(map(str, input().split())))

snake_able_map = [[True for i in range(N)] for j in range(N)]


apple_map = [[False for i in range(N)] for j in range(N)]

for apple in apples:
    apple_map[apple[0] - 1][apple[1] - 1] = True

# 시뮬레이션 시작
turn_idx = 0
time = 0
row, col = 0, 0

# 동, 남, 서, 북
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

direction_idx = 0

tail_row, tail_col = 0, 0

trace = []
turn_time = int(turns[turn_idx][0])
trace.append([0, 0])

while True:

    nrow = row + direction[direction_idx][0]
    ncol = col + direction[direction_idx][1]

    # 이동할려는 칸이 밖이라면 자기 자신과 닿으므로 break
    if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N:
        time += 1
        break

    # 상하좌우벽일 수도 있다.
    if not snake_able_map[nrow][ncol]:
        # print("G")
        time += 1
        break

    # 유효성 검사가 끝났다면 이제 이동을 한다.

    # 이동 할 현재 위치를 trace 에 기록
    snake_able_map[nrow][ncol] = False
    trace.append([nrow, ncol])
    # print(trace)
    if apple_map[nrow][ncol] == True:
        # 사과 먹음
        apple_map[nrow][ncol] = False
    else:

        tail_row, tail_col = trace.pop(0)
        # print("whiy? ", tail_row, tail_col)

        snake_able_map[tail_row][tail_col] = True

    # 움직이기 전에 turn 하는 지 확인한다.

    # 이동 !
    row = nrow
    col = ncol
    time += 1

    if time <= int(turns[-1][0]):

        # 움직이는 지 확인 검사.
        if time == turn_time:
            # 시계방향
            if turns[turn_idx][1] == 'D':
                direction_idx = (direction_idx + 1) % 4

            # 반시계 방향
            if turns[turn_idx][1] == 'L':
                direction_idx = (direction_idx - 1) % 4

            if turn_idx < len(turns)-1:
                turn_idx += 1
                turn_time = int(turns[turn_idx][0])

print(time)