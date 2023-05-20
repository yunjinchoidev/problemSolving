from collections import Counter
import sys

input = sys.stdin.readline

T = int(input())
N = int(input())
array1 = list(map(int, input().split()))
M = int(input())
array2 = list(map(int, input().split()))

prefix_A = []

for i in range(N):
    for j in range(i, N, 1):
        prefix_A.append(sum(array1[i : j + 1]))

prefix_B = []
for i in range(M):
    for j in range(i, M, 1):
        prefix_B.append(sum(array2[i : j + 1]))

# print(prefix_A)
# print(prefix_B)

# prefix_A.sort()
# prefix_B.sort()
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

countor_prefix_A = Counter(prefix_A)
countor_prefix_B = Counter(prefix_B)
# print(countor_prefix_A)
# print(countor_prefix_B)

answer = 0
for key, value in countor_prefix_A.items():
    # m = binary_search(prefix_B, T - key, 0, len(prefix_B) - 1)

    # print(key, countor_prefix_B[T - key] )
    if T - key in countor_prefix_B:
        answer += value * countor_prefix_B[T - key]

print(answer)
