# BFS
# from collections import deque
# def solution(triangle):
#     answer = 0
#     result = []
#
#     def bfs(n):
#         d = deque()
#         d.append((triangle[n][0], 0, 0))
#
#         while d:
#             x, y, z = d.popleft()
#             if y == len(triangle) - 1:
#                 result.append(x)
#
#             if y < len(triangle) - 1:
#                 d.append((x + triangle[y + 1][z], y + 1, z))
#                 d.append((x + triangle[y + 1][z + 1], y + 1, z + 1))
#
#     print(result)
#     bfs(0)
#     print(result)
#     answer = max(result)
#     return answer

# DP
def solution(triangle):
    answer = 0

    dp = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]

    dp[0][0] = triangle[0][0]

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][0] + triangle[i][0]
            elif j == len(dp[i]) - 1:
                dp[i][j] = dp[i - 1][len(dp[i - 1]) - 1] + triangle[i][len(dp[i]) - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    answer = max(dp[len(triangle) - 1])
    return answer