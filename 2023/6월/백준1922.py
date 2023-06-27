N = int(input())
M = int(input())
graph = [[] for i in range(N + 1)]

# for i in range(M):

# graph[s].append((e, d))
# graph[e].append((s, d))

parent = [i for i in range(N + 1)]

# print(parent)


def find_parent(parent, v):

    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])

    return parent[v]


def union(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


edges = []

for i in range(M):
    s, e, d = map(int, input().split())
    edges.append((d, s, e))

edges.sort()
cost = 0
for edge in edges:
    d, s, e = edge
    # print(d,s,e)
    if find_parent(parent, s) != find_parent(parent, e):  # 사이클이 아닌경우
        union(s, e)
        cost += d

print(cost)
