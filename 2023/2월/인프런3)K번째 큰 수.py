# Combinataion 을 이용한 풀이

from itertools import combinations

N, K = map(int, input().split())

cards = list(map(int, input().split()))
print(cards)
r = []

r = list(combinations(cards, 3))

rr = []
for _ in r:
    rr.append(sum(_))

rr.sort(reverse=True)
print(rr[K - 1])


# set 이용한 풀이

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res)
res.sort(reverse=True)
print(r)

# 3 중 for 문이지만 범위가 적어서 완전탐색으로 풀어도 좋다.
