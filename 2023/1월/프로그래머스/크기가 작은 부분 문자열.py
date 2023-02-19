def solution(t, p):
    answer = 0
    x = len(p)
    t_list = list(map(int, t))
    for i in range(len(t_list) - x + 1):

        u = ''.join(str(k) for k in t_list[i:i + x])

        if int(u) <= int(p):
            answer += 1

    return answer