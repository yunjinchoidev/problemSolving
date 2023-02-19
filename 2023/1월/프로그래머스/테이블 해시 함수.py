def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    s_list = []
    for i in range(row_begin - 1, row_end):
        k = 0
        for j in range(len(data[i])):
            k += data[i][j] % (i + 1)

        s_list.append(k)

    while len(s_list) != 1:
        x = s_list.pop()
        y = s_list.pop()
        s_list.append(x ^ y)

    answer = s_list[0]
    return answer