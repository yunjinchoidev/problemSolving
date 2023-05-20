def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    l = [31, 30, 28]
    for i in range(len(privacies)):
        x, t = privacies[i].split(" ")
        y, m, d = map(int, x.split("."))

        for j in range(len(terms)):
            if t == terms[j].split(" ")[0]:
                m += int(terms[j].split(" ")[1])

                if m > 12 and m % 12 != 0:
                    y += int(m / 12)
                    m -= int(m / 12) * 12
                if m > 12 and m % 12 == 0:
                    y += int(m / 12) - 1
                    m = 12

                if d == 1:
                    m -= 1
                    d = 28
                    if m == 0:
                        m = 12
                        y -= 1
                else:
                    d -= 1

        print(i)
        print(y, m, d)
        if t_y == y and t_m == m and t_d == d:
            continue
        if t_y > y:
            answer.append(i + 1)
            continue
        if t_y == y and t_m > m:
            answer.append(i + 1)
            continue
        if t_y == y and t_m == m and t_d > d:
            answer.append(i + 1)
            continue

    return answer
