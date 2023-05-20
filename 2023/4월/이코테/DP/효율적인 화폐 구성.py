N, M = map(int, input().split())
moneys = [int(input()) for i in range(N)]
moneys.sort(reverse=True)

dp = [100001 for i in range(100001)]
dp[0] = -1

for money in moneys:
    dp[money] = 1

for i in range(0, M + 1):
    x = float("inf")

    if i in moneys:
        dp[i] = 1
        continue

    for money in moneys:
        if i - money < 0:
            continue

        if dp[i - money] != -1:
            x = min(x, dp[i - money])

    if x != float("inf"):
        dp[i] = x + 1
    else:
        dp[i] = -1

# print(dp[:100])
print(dp[M])
