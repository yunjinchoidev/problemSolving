T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    new_numbers = numbers[s-1:e]
    new_numbers.sort()
    print(i+1, new_numbers[k-1])

