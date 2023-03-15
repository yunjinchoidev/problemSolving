N = int(input())
numbers = list(map(int, input().split()))

# 최솟값부터 확인한다.
numbers.sort()

idx = 0
start_number = 1
check_list = []

while True:
    x = check_list.copy()

    for i in range(len(x)):
        x[i] += numbers[idx]

    check_list.append(numbers[idx])
    check_list = check_list + x

    if start_number not in set(check_list):
        print(start_number)
        break
    else:
        idx += 1
        start_number += 1

        if idx == len(numbers):
            break

while True:
    if start_number not in set(check_list):
        print(start_number)
        break
    else:
        start_number += 1

