def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and stack[-1] < num and k >= 1:
            stack.pop()
            k -= 1
        stack.append(num)

    if k >= 1:
        for i in range(k):
            stack.pop()

    answer = ''.join(stack)
    return answer



# 스택을 생각하지 못한 채로
# 콤비네이션 사용 => 시간 초과
# Stack !