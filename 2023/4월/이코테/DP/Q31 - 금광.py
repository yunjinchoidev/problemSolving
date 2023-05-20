import sys
from pprint import pprint


def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    map_ = [[] for i in range(N)]
    numbers = list(map(int, input().split()))
    for r in range(N):
        for c in range(M):
            map_[r].append(numbers[r * M + c])

    pprint(map_)

    prefix_map = [[0 for i in range(M)] for j in range(N)]

    for c in range(M):
        for r in range(N):
            if c == 0:
                prefix_map[r][c] = map_[r][c]
            else:
                x = 0
                for i in range(-1, 2, 1):
                    if 0 <= r + i < N:
                        x = max(x, prefix_map[r + i][c - 1])
                prefix_map[r][c] = x + map_[r][c]

    answer = 0
    for c in range(N):
        answer = max(answer, prefix_map[c][M - 1])

    pprint(prefix_map)
    print(answer)
