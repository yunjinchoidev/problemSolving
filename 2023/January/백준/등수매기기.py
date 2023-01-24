import heapq
import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(N)]
heapq.heapify(numbers)
answer = 0
for i in range(N):
    x = abs(i+1 - heapq.heappop(numbers))
    answer += x
print(answer)
