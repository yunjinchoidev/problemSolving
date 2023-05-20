import math

N = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def felindrom(n):
    numbers = list(str(n))
    if len((numbers)) % 2 == 0:
        for i in range(len(numbers)):
            if numbers[i] != numbers[len(numbers) - 1 - i]:
                return False
        return True
    else:
        for i in range(len(numbers)):
            if numbers[i] != numbers[len(numbers) - 1 - i]:
                return False
            if i == int(len(numbers) / 2) + 1:
                break
        return True


while True:
    if N == 1:
        print(2)
        break

    if isPrime(N) and felindrom(N):
        print(N)
        break
    else:
        N += 1
