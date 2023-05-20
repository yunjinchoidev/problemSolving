from collections import deque

N, K = map(int, input().split())
numbers = deque(list(map(int, input().split())))

lv = 1
robot = deque([False for i in range(N)])
while True:
    # 돌리기
    numbers.rotate()
    robot.rotate()

    robot[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] == True and robot[i + 1] == False and numbers[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            numbers[i + 1] -= 1

    robot[N - 1] = False
    if numbers[0] > 0:
        robot[0] = True
        numbers[0] -= 1
    if numbers.count(0) >= K:
        break

    lv += 1

print(lv)
