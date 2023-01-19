def solution(lottos, win_nums):
    answer = []
    cnt = 0
    ok = 0
    the = 0
    for i in range(len(win_nums)):
        if lottos[i] == 0:
            cnt += 1
        else:
            if lottos[i] in win_nums:
                ok += 1
    if ok <= 1:
        the = 6
    else:
        the = 7 - ok
    the2 = the - cnt

    if the2 <= 0:
        answer.append(1)
    else:
        answer.append(the2)
    print(the, the2)
    answer.append(the)

    return answer