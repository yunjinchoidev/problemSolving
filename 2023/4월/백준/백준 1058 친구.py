import sys
input = sys.stdin.readline

N = int(input())
map_ = [list(map(str, input())) for _ in range(N)]
f = [[0 for i in range(N)] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if map_[i][j] == 'Y':
                f[i][j] = 1
            elif map_[i][k] == 'Y' and map_[k][j] == 'Y':
                f[i][j] = 1

m = float('-inf')
for r in range(N):
    for c in range(N):
        m = max(m, sum(f[r]))

print(m)
