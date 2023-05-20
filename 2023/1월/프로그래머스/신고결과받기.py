from collections import Counter


def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    r = []
    s = {}
    s = set(report)

    for i in s:
        x, y = i.split(" ")
        r.append(y)
    r_list = Counter(r)
    # print(r_list)
    check = []
    for idx, value in r_list.items():
        if value >= k:
            check.append(idx)

    for w in check:
        # print(idx)
        for j in range(len(id_list)):
            x = ""
            x += str(id_list[j])
            x += " "
            x += str(w)
            if str(x) in s:  # s 에서 검사해야 한다.
                answer[j] += 1

    return answer
