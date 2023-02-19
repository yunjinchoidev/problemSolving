def solution(num, total):
    answer = []

    numbers = [i for i in range(-1000, 1001, 1)]

    for i in range(0, 2001, 1):
        x = sum(numbers[i: i + num])
        if x == total:
            answer = numbers[i: i + num]
            break

    return answer