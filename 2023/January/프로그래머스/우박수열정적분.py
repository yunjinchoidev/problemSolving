def solution(k, ranges):
    answer = []
    x = [k]
    ch = k
    while ch != 1:
        if ch % 2 == 0:
            ch = int(ch / 2)
            x.append(ch)
        else:
            ch = ch * 3 + 1
            x.append(ch)
        if ch > 1:
            continue
        else:
            break

    s = []
    print(x)
    qq = len(x)
    for i in range(len(x) - 1):
        q = (x[i] + x[i + 1]) / 2
        s.append(q)

    for i in range(len(ranges)):
        m = ranges[i]
        x = m[0]
        y = qq + m[1]
        if x < y:
            answer.append(sum(s[x:y - 1]))
        else:
            answer.append(-1)

    print(s)
    return answer