import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

s_numbers = list(map(int, input().split()))
d_numbers = list(map(int, input().split()))

origin_numbers = [0 for i in range(N)]
for j in range(K):
    tmp = [0] * N
    for i in range(N):
        tmp[d_numbers[i] - 1] = s_numbers[i]
    s_numbers = tmp

    # s_numbers = [s_numbers[d_numbers[i]-1] for i in range(N)]


print(*s_numbers)