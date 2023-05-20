N = int(input())

origin = N
cnt = 0
while True:
    if N < 10:
        numbers = [0, N]
    else:
        numbers = list(map(int, str(N)))

    N = sum(numbers)
    N_list = list(map(int, str(N)))
    N = int(numbers[-1]) * 10 + int(N_list[-1])
    cnt += 1

    if origin == N:
        break
print(cnt)
