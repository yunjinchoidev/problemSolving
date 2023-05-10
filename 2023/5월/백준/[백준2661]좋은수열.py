import sys

N = int(input())


number = int(10**(N-1))


result = []

def check(result, addStr):
    temp = "".join(result) + addStr
    for i in range(1, len(temp) // 2 + 1):
        # print(temp[-2 * i : -1 * i])
        # print(temp[-1 * i :])

        if temp[-2 * i : -1 * i] == temp[-1 * i :]:
            return False

    return True

answer = []
def back():

    global result

    if len(result) == N:
        answer.append(int(''.join(result)))
        print(int(''.join(result)))
        exit()


    for i in range(1, 4):
        if check(result, str(i)):
            result.append(str(i))
            back()
            result.pop()


back()

