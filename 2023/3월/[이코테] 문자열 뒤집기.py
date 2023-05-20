N = input()
strings = list(map(str, N))

answer = 0

for i in range(len(strings) - 1):
    if strings[i] != strings[i + 1]:
        answer += 1

if answer % 2 == 0:
    print(int(answer / 2))
else:
    print(int(answer // 2) + 1)
