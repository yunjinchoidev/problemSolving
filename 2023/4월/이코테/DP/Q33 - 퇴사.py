import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
schedules = [list(map(int, input().split())) for i in range(N)]
schedules.insert(0, [0, 0])

dp = [0 for i in range(N + 1)]

# i 번째 날을 사용해야 하는 날짜들 중에서 최댓값을 더한 것이 dp[i] 다.
for i in range(1, len(schedules)):
    dp[i] = dp[i - 1]
    for j in range(1, i+1):
        if j + schedules[j][0] - 1 == i:
            dp[i] = max(dp[i], dp[i - schedules[j][0]] + schedules[j][1])

print(dp[-1])
