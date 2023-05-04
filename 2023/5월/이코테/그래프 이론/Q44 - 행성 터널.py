import sys

N = int(input())
planets = [list(map(int, input().split())) for i in range(N)]


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
for i in range(N):
    for j in range(i, N):
        edges.append((min(abs(planets[i][0] - planets[j][0]),
                          abs(planets[i][1] - planets[j][1]),
                          abs(planets[i][2] - planets[j][2]))
                      , i, j))

edges.sort()

result = []
for edge in edges:
    cost, s, e = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        result.append(cost)
    #
    # if len(result) == N:
    #     break

# print(planets)
print(sum(result))
