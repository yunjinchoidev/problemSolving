N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
height = numbers[0]

idx = 1
s = 0
answer = 0
# for i in range(height-1, 1, -1):
#     if i < numbers[idx]:
#         idx +=1
#         s += idx
#     else:
#         s += idx
#
#     print(i, s, idx)
#     if s >= M:
#         answer = i
#         break
#
# print(answer)

def binary_search(start, end, numbers, M):
    if start > end:
        return None
    mid = (start+end)//2
    s = 0
    for number in numbers:
        if number > mid:
            s += number - mid
    if s >= M:
        return binary_search(mid+1, end, numbers, M)
    else:
        return binary_search(start, mid-1, numbers, M)

numbers.sort()

while True:
    if binary_search(0, height, numbers, M):
        answer = binary_search(0, height, numbers, M)
        break