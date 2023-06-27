N, M = map(int, input().split())

# graph = [[] for i in range(N+1)]
#
# for i in range(M):
#     s, e = map(int, input())
#     graph[s].append(e)
#     graph[e].append(s)

map_ = [[int(1e9) for i in range(N+1)] for j in range(N+1)]
for i in range(N+1):
    map_[i][i] = 0

for i in range(M):
    s, e = map(int, input().split())
    map_[s][e] = 1
    map_[e][s] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            map_[i][j] = min(map_[i][j], map_[i][k]+map_[k][j])

# print(map_)
result = [int(1e9)]
for r in range(1, N+1):
    result.append(sum(map_[r][1:]))

# print(result)
print(result.index(min(result)))
