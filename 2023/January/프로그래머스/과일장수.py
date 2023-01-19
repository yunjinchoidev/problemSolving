def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        if i > len(score) - m:
            break

        answer += m * score[i + m - 1]

    return answer