def solution(s):
    answer = -1

    s_list = list(s)
    stack = []

    for i in s_list:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if len(stack) >= 1:
        answer = 0
    else:
        answer = 1

    return answer


# 스택을 이용해 간단하게 풀 수 있다.. .
