def solution(s):
    answer = []
    s_list = list(s)
    print(s_list)
    k_set = {}
    for idx, value in enumerate(s_list):
        print(idx, value)
        if value not in k_set :
            k_set[value] = idx
            answer.append(-1)
        else :
            answer.append(idx - k_set[value])
            k_set[value] = idx
    print(k_set)
    print(answer)
    return answer
