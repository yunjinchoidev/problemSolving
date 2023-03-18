import sys
from string import ascii_lowercase

input = sys.stdin.readline
position = input()
answer = 0

col, row = position[0], int(position[1])
print(col, row)

col = ascii_lowercase.index(col) + 1

move_col = [2, 2, 1, -1]
move_row = [1, -1, 2, 2]

for i in range(4):
    ncol = col + move_col[i]
    nrow = row + move_row[i]
    if ncol < 1 or ncol > 8 or nrow < 1 or nrow > 8:
        continue
    answer += 1

print(answer)