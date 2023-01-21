from collections import deque


def solution(progresses, speeds):
    d = deque(progresses)
    s = deque(speeds)
    answer = []
    while True:
        for i in range(len(d)):
            d[i] += s[i]

        if d[0] >= 100:
            cnt = 0
            while d:
                if d[0] >= 100:
                    d.popleft()
                    s.popleft()
                    cnt += 1
                else:
                    break
            answer.append(cnt)

        if d:
            continue
        else:
            break
    print(answer)
    return answer

solution([93, 30, 55], [1, 30, 5])