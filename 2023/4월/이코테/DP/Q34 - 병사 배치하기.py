import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
soldiers = list(map(int, input().split()))
soldiers.insert(0, 0)

dp = [1 for i in range(2001)]
dp[0] = 0
dp[1] = 1

for i in range(2, N+1):
    for j in range(1, i+1):
        if soldiers[i-j] <= soldiers[i]: # 뒤쪽 군인이 군사력이 더 크다면
            continue
        else: # 정상인 경우
            dp[i] = max(dp[i], dp[i - j]+1)


# print(dp)
print(N-max(dp))