from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

answer = 0

idx = 0

left = numbers[:idx + 1]
right = numbers[idx + 2:]

print(left, right)

lm = max(left)
rm = max(right)

r = []
r.append(lm+ rm)

left_dp = [0 for i in range(N)]
right_dp = [0 for i in range(N)]

for i in range(1, N - 2):
    lm = max(numbers[:i + 1])
    rm = max(numbers[i + 2:])
    r.append(rm + lm)

print(r)
print(max(r))

rr = []
for i in range(1, N -2):
    left_dp[i] = max(left_dp[i-1], numbers[i])
    right_dp[i] = max(right_dp[i-1], numbers[i])
    rr.append(left_dp[i] + right_dp[i])

print(rr)
print(max(rr))