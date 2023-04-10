N, M = map(int, input().split())
moneys = [int(input()) for i in range(N)]
moneys.sort(reverse=True)

dp = [-1 for i in range(100001)]
dp[0] = -1

for money in moneys:
    dp[money] = 1

for i in range(moneys[0]+1, M+1):
    x = float('inf')
    for money in moneys:
        if dp[i-money] != -1 : # 만들 수 있다는 것.
            x = min(x, dp[i-money])

    if x != float('inf'):
        dp[i] = x + 1
    else:
        dp[i] = -1

print(dp[M])