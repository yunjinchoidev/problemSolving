from collections import deque


def solution(p):
    answer = ''

    def is_balance_string(input_string):
        if input_string.count("(") == input_string.count(")"):
            return True
        return False

    def separate_u_v(p):  # 문자열 p를 u와 v로 분리
        # u : 균형잡힌 괄호 문자열, v : 나머지
        open_p, close_p = 0, 0
        for i in range(len(p)):
            if p[i] == '(':
                open_p += 1
            else:
                close_p += 1
            if open_p == close_p:
                return p[:i + 1], p[i + 1:]  # u, v

    def is_correct_string(input_string):
        stack = []
        idx = 0

        while True:
            if not stack:
                stack.append(input_string[idx])
            else:
                if stack[-1] == "(" and input_string[idx] == ")":
                    stack.pop()
                else:
                    stack.append(input_string[idx])

            idx += 1
            if idx >= len(input_string):
                break

        if stack:
            return False
        else:
            return True

    def check_balance(u):  # 문자열 u가 올바른 괄호 문자열인지 체크
        stack = deque()
        for i in u:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    return False
                stack.pop()
        return True if not stack else False

    def get_reverse_string(strings):
        r = {"(": ")", ")": "("}
        return [r[s] for s in strings]

    def check(s):

        if s == '':
            return ''

        u, v = separate_u_v(s)  # 과정 2

        if check_balance(u):
            return u + check(v)
        else:
            r = "("
            r += check(v)
            r += ")"
            r += get_reverse_string(s[1:-1])
            return r

        #         for i in range(len(s)):

    #             if not is_balance_string(s[:i]) or not is_balance_string(s[i:]):
    #                 continue
    #             else :
    #                 print("GGGGG")
    #                 print(s[:i])

    # if is_correct_string(s[:i]):
    # v = check(s[i:])
    # return s[:i] + v
    #                 else :
    #                     r = "("
    #                     r += check(s[i:])
    #                     r += ")"
    #                     r += get_reverse_string(s[1:-1])
    #                     return r

    def t(p):
        if not p:  # 과정 1
            return p

        u, v = separate_u_v(p)  # 과정 2

        if check_balance(u):  # 과정 3
            return u + solution(v)  # 과정 3-1
        else:  # 과정 4
            answer = '('  # 과정 4-1
            answer += solution(v)  # 과정 4-2
            answer += ')'  # 과정 4-3

            for pp in u[1:len(u) - 1]:  # 과정 4-4
                if pp == '(':
                    answer += ')'
                else:
                    answer += '('
        return answer  # 과정 4-5

        if p == '':
            return answer

    answer = t(p)
    return answer
