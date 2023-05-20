from collections import deque


def solution(s):
    answer = 0

    s_list = deque(s)

    d = s_list
    for q in range(len(s)):
        stack = []
        cnt = 0
        for i in range(len(d)):
            if d[i] == "[" or d[i] == "{" or d[i] == "(":
                stack.append(d[i])
                cnt += 1
                continue
            if stack:
                if d[i] == "]" and stack[-1] == "[":
                    stack.pop()
                    cnt += 1
                    continue
                if d[i] == "}" and stack[-1] == "{":
                    stack.pop()
                    cnt += 1
                    continue
                if d[i] == ")" and stack[-1] == "(":
                    stack.pop()
                    cnt += 1
                    continue
        if len(stack) == 0 and cnt == len(s):
            answer += 1

        d.rotate()

        print(len(stack))

    print(stack)

    return answer
