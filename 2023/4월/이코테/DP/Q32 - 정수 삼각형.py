N = int(input())
triangle = [[] for i in range(N)]
for i in range(N):
    triangle[i] = list(map(int, input().split()))

# print(triangle)

dp = [[0 for c in range(len(triangle[r]))] for r in range(N)]

for r in range(N):
    for j in range(len(triangle[r])):
        if j == 0:
            dp[r][j] = triangle[r][j] + dp[r - 1][0]
        elif j == len(triangle[r]) - 1:
            dp[r][j] = triangle[r][j] + dp[r - 1][len(triangle[r - 1]) - 1]
        else:
            dp[r][j] = triangle[r][j] + max(dp[r - 1][j - 1], dp[r - 1][j])


answer = 0
for i in range(N):
    answer = max(answer, dp[N - 1][i])

# print(dp)
print(answer)
