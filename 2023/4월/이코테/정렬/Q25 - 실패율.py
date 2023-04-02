from collections import Counter


def solution(N, stages):
    answer = []
    x = Counter(stages)
    stages.sort()
    s = set(stages)

    fail = [[i, 0] for i in range(N + 2)]
    visited = [False for i in range(N + 2)]

    for i in range(len(stages)):
        if not visited[stages[i]]:
            visited[stages[i]] = True
            fail[stages[i]][1] = x[stages[i]] / (len(stages) - i)

    del fail[0]
    del fail[len(fail) - 1]

    qq = sorted(fail, key=lambda x: (-x[1], x[0]))
    print(qq)
    for i in qq:
        answer.append(i[0])

    return answer