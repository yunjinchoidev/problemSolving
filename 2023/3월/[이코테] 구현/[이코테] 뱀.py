# https://www.acmicpc.net/problem/3190
import sys
from pprint import pprint

input = sys.stdin.readline

N = int(input())
apple_cnt = int(input())

apples = []

for i in range(apple_cnt):
    apples.append(list(map(int, input().split())))

move_cnt = int(input())
moves = []
for i in range(move_cnt):
    moves.append(list(map(str, input().split())))

can_map = [['✅' for i in range(N)] for j in range(N)]

can_map[0][0] = False
can_map[N - 1][N - 1] = False
can_map[0][N - 1] = False
can_map[N - 1][0] = False

apple_map = [[False for i in range(N)] for j in range(N)]

for apple in apples:
    apple_map[apple[0] - 1][apple[1] - 1] = '🟥'

# 시뮬레이션 시작
move_idx = 0
time = 0
row, col = 0, 0

# 오, 왼, 상, 하
# nrow = [1, -1, 0, 0]
# ncol = [0, 0, -1, 1]

# 동, 남, 서, 북
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

direction_idx = 0

end_row, end_col = 0, 0

trace = []
move_time = int(moves[move_idx][0])
trace.append([0, 0])

while True:

    time += 1
    nrow = row + direction[direction_idx][0]
    ncol = col + direction[direction_idx][1]

    if move_time != -1:
        move_time = int(moves[move_idx][0])

    if time == move_time:
        if moves[move_idx][1] == 'D':
            direction_idx = (direction_idx + 1) % 4
        if moves[move_idx][1] == 'L':
            direction_idx = (direction_idx + 3) % 4

        move_idx += 1
        if move_idx == len(moves):
            move_time = -1

    if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N:
        # print("GG")
        if trace:
            # print(trace)
            end_row, end_col = trace.pop(0)
            can_map[end_row][end_col] = True
        break
        # continue

    if not can_map[nrow][ncol]:
        break

    if apple_map[nrow][ncol] == '🟥':
        # print("사과머금")
        can_map[nrow][ncol] = False
    else:
        can_map[nrow][ncol] = False
        if trace:
            # print(trace)
            end_row, end_col = trace.pop(0)
            can_map[end_row][end_col] = '✅'

    row = nrow
    col = ncol

    trace.append([row, col])

    # print("GGGGGGGGG")
    # print(time)
    # pprint(can_map)

print(time)
# print(trace)
