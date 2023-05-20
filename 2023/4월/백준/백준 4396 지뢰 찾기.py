N = int(input())

map_ = [list(map(str, input())) for _ in range(N)]
played_map = [list(map(str, input())) for _ in range(N)]
result = [[0] * N for _ in range(N)]

# 좌하 하 우하 왼 우 왼상 상 우상
nr = [-1, -1, -1, 0, 0, 1, 1, 1]
nc = [-1, 0, 1, -1, 1, -1, 0, 1]

jiroi = False
for i in range(N):
    for j in range(N):
        if played_map[i][j] == "x" and map_[i][j] == "*":
            jiroi = True
        if played_map[i][j] == "x":
            for k in range(8):
                nr_ = i + nr[k]
                nc_ = j + nc[k]
                if 0 <= nr_ < N and 0 <= nc_ < N:
                    if map_[nr_][nc_] == "*":
                        result[i][j] += 1
        else:
            result[i][j] = "."

if jiroi:
    for i in range(N):
        for j in range(N):
            if map_[i][j] == "*":
                result[i][j] = "*"

for i in range(N):
    for j in range(N):
        print(result[i][j], end="")
    print()
