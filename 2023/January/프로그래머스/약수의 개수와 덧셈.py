def solution(left, right):
    answer = 0

    def divi_cnt(n):
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1

        if cnt % 2 == 1:
            return -1
        return 1

    for i in range(left, right + 1):
        print(i, divi_cnt(i))
        answer += i * divi_cnt(i)

    return answer