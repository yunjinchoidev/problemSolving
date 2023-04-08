import sys
import heapq
input = sys.stdin.readline

n = int(input())

day_money = [tuple((map(int, input().split()))) for _ in range(n)]

day_money.sort(key=lambda x: x[1]) # 날짜 오름차순

lectures = []

for dm in day_money: # 날짜 오름차순으로 순회
    heapq.heappush(lectures, dm[0]) # 강의 가격을 힙에 넣음
    if len(lectures) > dm[1]: # 강의 날짜 수가 이때의 날짜 한도보다 크면
        heapq.heappop(lectures) # 빼줌. 이때 가장 작은 값이 빠짐 (최소 힙) 큰 것부터 넣으므로.

print(sum(lectures))

#
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# schedules = [0] * 10001
# lectures = []
# for _ in range(n):
#     pay, day = map(int, input().split())
#     lectures.append((pay, day))
#
# lectures.sort(key=lambda x: (-x[0]))
#
# for i in range(n):
#   for j in range(lectures[i][1], 0, -1):
#     if schedules[j] == 0:
#       schedules[j] += lectures[i][0]
#       break
#
# print(sum(schedules))