import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())

numbers = list(map(int, input().split()))

# print(numbers)

d = deque(numbers)

robo = [False for i in range(N)]
robots = deque(robo)

idx = 0
while True:
    idx += 1

    # step 1
    d.rotate()
    robots.rotate()

    robots[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and d[i + 1] >= 1:
            # print(i)
            robots[i] = False
            robots[i + 1] = True
            d[i + 1] -= 1

            robots[N - 1] = False

    if d[0] != 0 and not robots[0]:
        robots[0] = True
        d[0] -= 1

    # print(robots)
    # print(d)

    # if idx == 10:
    #     break
    if d.count(0) >= K:
        break

    # print(idx)

# print(d)
print(idx)
