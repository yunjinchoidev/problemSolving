import sys

input = sys.stdin.readline

N = int(input())
moves = list(map(str, input().split()))

x, y = 1, 1
for move in moves:
    if move == 'U':
        if x == 1:
            continue
        x -= 1
    elif move == 'D':
        if x == N:
            continue
        x += 1
    elif move == 'L':
        if y == 1:
            continue
        y -= 1
    elif move == 'R':
        if y == N:
            continue
        y += 1

print(x, y)