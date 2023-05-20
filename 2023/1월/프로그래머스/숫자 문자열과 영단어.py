def solution(s):
    answer = 0
    s_list = s
    ss = ""
    i = 0
    while True:
        if s_list == "":
            break

        if s_list[i].isdigit():
            ss += str(s_list[i])
            s_list = s_list[:i] + s_list[i + 1 :]
            continue

        if s_list[i : i + 3] == "one":
            s_list = s_list[:i] + s_list[i + 3 :]
            ss += "1"
            i = 0
            continue

        if s_list[i : i + 3] == "six":
            s_list = s_list[:i] + s_list[i + 3 :]
            ss += "6"
            i = 0
            continue

        if s_list[i : i + 3] == "two":
            s_list = s_list[:i] + s_list[i + 3 :]
            ss += "2"
            i = 0
            continue

        if s_list[i : i + 4] == "zero":
            s_list = s_list[:i] + s_list[i + 4 :]
            ss += "0"
            i = 0
            continue

        if s_list[i : i + 4] == "four":
            s_list = s_list[:i] + s_list[i + 4 :]
            ss += "4"
            i = 0
            continue

        if s_list[i : i + 4] == "five":
            s_list = s_list[:i] + s_list[i + 4 :]
            ss += "5"
            i = 0
            continue

        if s_list[i : i + 4] == "nine":
            s_list = s_list[:i] + s_list[i + 4 :]
            ss += "9"
            i = 0
            continue

        if s_list[i : i + 5] == "three":
            s_list = s_list[:i] + s_list[i + 5 :]
            ss += "3"
            i = 0
            continue

        if s_list[i : i + 5] == "seven":
            s_list = s_list[:i] + s_list[i + 5 :]
            ss += "7"
            i = 0
            continue

        if s_list[i : i + 5] == "eight":
            s_list = s_list[:i] + s_list[i + 5 :]
            ss += "8"
            i = 0
            continue
    print(ss)
    answer = int(ss)
    return answer
