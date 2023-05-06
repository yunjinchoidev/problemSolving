import heapq
from collections import deque
import itertools

T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    d = deque(numbers)


    idx = 0
    while d:
        m = max(d)

        if d[0] == m:
            idx += 1
            d.popleft()
            if M == 0:
                print(idx)
                break
            else:
                M -= 1
        else:
            d.rotate(-1)
            if M == 0:
                M = len(d) - 1
            else:
                M -= 1

