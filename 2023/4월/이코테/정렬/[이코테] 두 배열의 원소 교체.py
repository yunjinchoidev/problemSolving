N, K = map(int, input().split())

array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort()

answer = sum(array_A)
for i in range(K):
    answer -= array_A[i]
    answer += array_B[N - 1 - i]

print(answer)
