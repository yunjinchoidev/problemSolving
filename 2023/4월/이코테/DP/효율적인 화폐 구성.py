N, M = map(int, input().split())
moneys = [int(input()) for i in range(N)]
moneys.sort(reverse=True)

dp = [9999999 for i in range(M+1)]
dp[0] = 0

for money in moneys:
    dp[money] = 1

for i in range(max(moneys)+1, M+1):
    flag = False
    for money in moneys:
        if i % money == 0:
            dp[i] = dp[i//money]+1
            flag = True
            break
    if not flag:
        dp[i] = -1

print(dp)
print(dp[M])