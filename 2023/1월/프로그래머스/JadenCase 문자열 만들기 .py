def solution(s):
    answer = ""
    x = s.lower().split(" ")

    for i in range(len(x)):
        if x[i] != "":
            x[i] = x[i][0].upper() + x[i][1:]

    print(x)
    print(answer)
    answer = " ".join(x)

    return answer
