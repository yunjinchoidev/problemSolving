def solution(word):
    answer = 0
    s = "AEIOU"
    r = []

    def all(cnt, start_word):
        if cnt == 5:
            return

        for i in range(len(s)):
            w = start_word + s[i]
            r.append(w)
            all(cnt + 1, w)

    all(0, "")
    answer = r.index(word) + 1
    return answer