N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

answer = sum(numbers)
idx = 0

r = []
for i in range(1, numbers[-1]):
    if i < numbers[idx]:
        answer -= (N - idx)
        answer += idx
    elif i == numbers[idx]:
        answer -= (N - idx)
        answer += idx
        idx += 1

    r.append((answer, i))

# print(r)
r.sort(key=lambda x: (x[0], x[1]))
print(min(r)[1])
