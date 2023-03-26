N = int(input())

numbers = list(map(int, input().split()))

cals = list(map(int, input().split()))

combination = []
combination_result = []

def DFS(cal_list, stack, num, depth):
    if sum(cal_list) == 0:
        combination.append(stack)
        combination_result.append(num)
        return

    for i in range(4):
        if cal_list[i] == 0:
            continue
        else:
            cal_list[i] -= 1
            stack += str(i)
            depth += 1
            temp_num = num
            if i == 0:
                num += numbers[depth]
            elif i == 1:
                num -= numbers[depth]
            elif i == 2:
                num *= numbers[depth]
            elif i == 3:
                num = int(num/numbers[depth])

            DFS(cal_list, stack, num, depth)
            cal_list[i] += 1
            stack = stack[:-1]
            num = temp_num
            depth -= 1

DFS(cals, '', numbers[0], 0)

print(max(combination_result))
print(min(combination_result))