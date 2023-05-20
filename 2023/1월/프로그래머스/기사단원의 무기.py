def get_cds(n, limit, power):
    cnt = 0
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            if i == n // i:
                cnt += 1
            else:
                cnt += 2
        if cnt > limit:
            return power
    return cnt


def solution(number, limit, power):
    total = 1
    for i in range(2, number + 1):
        len_cds = get_cds(i, limit, power)
        total += len_cds

    return total
