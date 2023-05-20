def solution(land):
    answer = 0

    dp = [[0 for i in range(4)] for i in range(len(land))]
    for i in range(4):
        dp[0][i] = land[0][i]

    # print(dp)
    for i in range(1, len(land)):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) + land[i][0]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3]) + land[i][1]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3]) + land[i][2]
        dp[i][3] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + land[i][3]

        # print(dp)
    answer = max(dp[len(land) - 1])

    return answer


## DP !
