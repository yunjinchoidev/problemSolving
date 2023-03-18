import sys
input = sys.stdin.readline

word = input()

digit_sum = 0

for i in range(len(word)):
    if word[i].isdigit():
        digit_sum += int(word[i])
    else:
        word = word[:i] + word[i:]

answer = word+str(digit_sum)
print(answer)
