import math

M, N = map(int, input().split())

result = [True for i in range(N+1)]
result[1] = 0

for i in range(2, int(math.sqrt(N))+1):
    if result[i]:
        j = 2

        while i * j <= N :
            result[i*j] = False
            j += 1


for i in range(M, N+1):
    if result[i]:
        print(i)
