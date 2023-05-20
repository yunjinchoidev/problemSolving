import sys

input = sys.stdin.readline
N = int(input())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (N + 1)
for i in range(0, N + 1):
    parent[i] = i

edges = []
x = []
y = []
z = []

for i in range(N):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))

edges.sort()

result = []
for edge in edges:
    cost, s, e = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        result.append(cost)

print(sum(result))
