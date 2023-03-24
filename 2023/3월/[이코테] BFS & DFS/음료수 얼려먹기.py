import sys
input = sys.stdin.readline


N, M = input().split()

map_ = [list(map(int, input())) for i in range(N)]

print(map_)
