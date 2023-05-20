def solution(s):
    answer = 0
    s_list = list(s)
    left_cnt = 0
    right_cnt = 0
    for i in range(len(s_list)):
        if i == len(s_list) - 1:
            answer += 1
            break

        if left_cnt == 0:
            x = s_list[i]
            left_cnt = 1
            right_cnt = 0
        else:
            if x == s_list[i]:
                left_cnt += 1
            else:
                right_cnt += 1
            if left_cnt == right_cnt:
                answer += 1
                left_cnt = 0
                right_cnt = 0

    return answer
