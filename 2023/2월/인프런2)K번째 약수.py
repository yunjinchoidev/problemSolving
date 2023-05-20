N, K = map(int, input().split())

order = 0
for i in range(1, N):
    if N % i == 0:
        order += 1

    if order == K:
        print(i)
        break
else:
    print(-1)
