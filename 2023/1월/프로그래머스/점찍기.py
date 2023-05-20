import math


def solution(k, d):
    answer = 0

    x_list = [i for i in range(0, d + 1, k)]

    for i in range(len(x_list)):
        max_y = int((int(float(math.sqrt(d**2 - x_list[i] ** 2)))) / k) + 1
        answer += max_y

    return answer
