def solution(k, score):
    answer = []
    s_list = []
    for i in range(len(score)):
        if i < k:
            if i == 0:
                s_list = [score[0]]
            else:
                s_list = score[0:i + 1]
            s_list.sort()
            # print(s_list)
            answer.append(s_list[0])
        else:
            s_list = score[0:i + 1]
            s_list.sort(reverse=True)
            # print(s_list)
            answer.append(s_list[k - 1])

    print(answer)

    return answer