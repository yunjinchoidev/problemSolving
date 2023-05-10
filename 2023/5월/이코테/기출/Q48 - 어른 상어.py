import sys

N, M, k = map(int, input().split())

# 상어 맵 (현재 상어 번호, 방향, 냄새 남긴 상어 번호, 남은 초)
map_ = [[] for r in range(N)]

for i in range(N):

    numbers = list(map(int, input().split()))

    for num in numbers:
        if num == 0:
            map_[i].append([0, 0, 0, 0])
        else:
            map_[i].append([num, 0, num, k])

init_direction = list(map(int, input().split()))

for r in range(N):
    for c in range(N):
        if map_[r][c][0] != 0:
            map_[r][c][1] = init_direction[map_[r][c][0] - 1] - 1  # 1 을 빼서 더해준다.

# 상어 맵
# 작을 수록 큼.
# M 개의 상어
# 냄새 뿌리기.
# 상하좌우 이동 . 냄새가 없는 칸으로 이동. 자기의 냄새가 있는 방향으로 이동. 특정 우선순위.
# 여러 마리가 있으면 작은 상어가 차지.



# %4 ~ %4 +3 까지가 i 번째 상어의 상하좌우 우선순위임.
prioritys = [list(map(int, input().split())) for i in range(M * 4)]

# 북 남 서 동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_all_sharks():
    sharks = []

    for r in range(N):
        for c in range(N):
            if map_[r][c][0] != 0:
                sharks.append([map_[r][c][0],
                               map_[r][c][1],
                               map_[r][c][2],
                               map_[r][c][3],
                               r, c]) # r,c 는 좌표임.

    # 작은 상어부터 이동해서 첫번째걸 가져오는 방식.
    sharks.sort()
    return sharks


# 특정 상어의 좋은 방향 찾기.
def find_direction(shark):

    global map_

    num, d, scent_num, second, r, c = shark

    priority = prioritys[(num - 1) * 4 + d]

    no_scent_direction = []
    my_scent_dirction = []
    move_direction = []


    for i in range(4):

        direc_flag = False

        # priority 에서 꺼내줄 때는 1  빼준 값으로.
        new_direction = priority[i] - 1

        # 우선 순위가 1 ~ 4 이므로 0 ~ 3 으로 빼주면 됨. 방향 순서는 일치함. (북남서동)
        nr = r + dr[new_direction]
        nc = c + dc[new_direction]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if map_[nr][nc][2] != 0 and map_[nr][nc][3] != 0:
            direc_flag = True

            if map_[nr][nc][2] == num:
                my_scent_dirction.append(new_direction)

        if not direc_flag:
            no_scent_direction.append(new_direction)

    # print(shark, no_scent_direction, my_scent_dirction, move_direction)

    # 우선 순위로 돌았으므로 0 번째 꺼를 리턴해주면 됨.
    if no_scent_direction:
        return no_scent_direction[0]

    if my_scent_dirction:
        return my_scent_dirction[0]

    if move_direction:
        return priority[0] - 1


# 모든 상어 이동하기.
def move_all_shark():
    global map_

    global k

    sharks = find_all_sharks()





    # 모든 상어에 대해 수행
    for shark in sharks:

        num, direc, sent_num, second, r, c = shark

        # 방향 최신화
        direc = find_direction(shark)

        nr = r + dr[direc]
        nc = c + dc[direc]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        dupli_shark_map_[nr][nc].append([num, direc, num, k, r, c])

    # for _ in dupli_shark_map_:
    #     print(_)

    for r in range(N):
        for c in range(N):

            if len(dupli_shark_map_[r][c]) >= 2:

                map_[r][c] = dupli_shark_map_[r][c][0][0:4]

                # 1 부터
                for i in range(1, len(dupli_shark_map_[r][c])):
                    num, direc, num, k, pre_r, pre_c = dupli_shark_map_[r][c][i]

                    map_[pre_r][pre_c][0] = 0 # 상어
                    map_[pre_r][pre_c][1] = 0 # 방향


            elif len(dupli_shark_map_[r][c]) == 1:

                num, direc, num, k, pre_r, pre_c = dupli_shark_map_[r][c][0]
                # print(f"???{dupli_shark_map_[r][c][0]}")

                map_[r][c] = [num, direc, num, k]
                map_[pre_r][pre_c][0] = 0
                map_[pre_r][pre_c][1] = 0

            # 아무 것도 없었으면 0, 0
            else:
                map_[r][c][0] = 0
                map_[r][c][1] = 0


    for r in range(N):
        for c in range(N):

            if map_[r][c][0] == 0:
                # 1 초만 남았으면
                if map_[r][c][3] == 1:
                    map_[r][c][2] = 0
                    map_[r][c][3] -= 1

                # 그 이상 남았으면
                elif map_[r][c][3] > 1:
                    map_[r][c][3] -= 1


# 1번 상어만 남아있는 지 여부 체크 함수
def is_only_first_shark():
    global map_

    for r in range(N):
        for c in range(N):
            if map_[r][c][0] != 0 and map_[r][c][0] != 1:
                return False

    return True


time = 0

while True:

    dupli_shark_map_ = [[[] for i in range(N)] for r in range(N)]

    # print(dupli_shark_map_[2][1])
    if is_only_first_shark():
        break

    time += 1



    move_all_shark()

    # for _ in map_:
        # print(_)

    # print(f"{time}----------------------------")

    if time >= 1000:
        time = -1
        break

print(time)
