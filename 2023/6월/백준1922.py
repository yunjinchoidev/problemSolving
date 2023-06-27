N = int(input())
M = int(input())

edges = []
for i in range(M):
    s, e, d = map(int, input().split())
    edges.append((d, s, e))

parent = [i for i in range(N + 1)]


def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])

    return parent[v]


def union(s, e):
    s = find_parent(parent, s)
    e = find_parent(parent, e)
    if s <= e:
        parent[e] = s
    else:
        parent[s] = e


result = 0
edges.sort()
for edge in edges:
    cost, s, e = edge
    if find_parent(parent, s) != find_parent(parent, e):
        union(s, e)
        result += cost
print(result)
