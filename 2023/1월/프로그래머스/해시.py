def solution(clothes):
    answer = 1
    dict = {}

    for i in range(len(clothes)):
        # print(clothes[i][0],clothes[i][1])
        if clothes[i][1] not in dict:
            dict[clothes[i][1]] = 1
        else:
            dict[clothes[i][1]] += 1
    # print(dict)

    for idx, value in dict.items():
        # print(idx, value)
        answer *= value + 1

    return answer - 1
