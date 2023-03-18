import sys

input = sys.stdin.readline

N = int(input())

answer = 0
result = []

hourThreeContainYn = False
minuitThreeContainYn = False
secondThreeContainYn = False

for hour in range(N + 1):

    if '3' in str(hour):
        hourThreeContainYn = True


    for minuit in range(60):
        if '3' in str(minuit):
            minuitThreeContainYn = True

        for second in range(60):
            if '3' in str(second):
                secondThreeContainYn = True

            if hourThreeContainYn or minuitThreeContainYn or secondThreeContainYn :
                answer += 1
                result.append([str(hour), str(minuit), str(second)])

            secondThreeContainYn = False
        minuitThreeContainYn = False
    hourThreeContainYn = False


print(answer)
