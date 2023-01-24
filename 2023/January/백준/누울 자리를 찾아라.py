N = int(input())

condo = [list(map(str, input())) for i in range(N)]
answer_row = 0
answer_col= 0

for row in condo:
    cnt = 0
    for j in row:
        if j == '.':
            cnt += 1
        elif j == 'X' and cnt >= 2:
            answer_row += 1
            cnt = 0
        elif j == 'X' and cnt <= 1:
            cnt = 0
    if cnt >= 2:
        answer_row += 1

for i in range(N):
    cnt = 0
    for j in range(N):

        if condo[j][i] == '.':
            cnt += 1
        elif condo[j][i] == 'X' and cnt >= 2:
            answer_col += 1
            cnt = 0
        elif condo[j][i] == 'X' and cnt <= 1:
            cnt = 0
    # print(i, cnt, answer_col)
    if cnt >= 2:
        answer_col += 1
    # print(i, cnt, answer_col)


print(answer_row, answer_col)
