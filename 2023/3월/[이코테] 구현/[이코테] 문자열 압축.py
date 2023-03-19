def solution(s):
    answer = float("inf")

    r = []

    # 1 ~
    for i in range(1, len(s) - 1):
        print(s)
        length = len(s)
        cnt = 1
        substring = ''
        # 문자열비교
        for j in range(0, len(s), i):

            if j + i >= len(s):
                continue

            if s[j:j + i] == s[j + i:j + 2 * i]:
                cnt += 1
            else:

                # 필요없는 식이지만 헷갈려서 적음.
                if cnt != 1:
                    length -= cnt * i
                    substring += str(cnt) + s[j:j + i]
                    cnt = 1
                    # print(s)
                else:
                    cnt = 1
                    substring += s[j:j + i]
                    # print(s)
        r.append([substring, i, length])
        # print(substring)
        answer = min(answer, length)
    print(r)
    return answer

solution('aabbaccc')