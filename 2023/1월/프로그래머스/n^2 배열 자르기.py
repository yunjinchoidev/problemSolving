# def solution(n, left, right):
#     answer = []
#     box = [[0 for j in range(n)] for i in range(n)]
#     # print(box)
#
#     r = []
#     check = 0
#     # print(box)
#     # print(divmod(left, n))
#     # print(divmod(right, n))
#     x, y = divmod(left, n)
#     x2, y2 = divmod(right, n)
#
#     for i in range(n):
#         cnt = 0
#         if i > x2 + 1:
#             break
#         for j in range(n):
#             if cnt <= i:
#                 box[i][j] = i + 1
#                 cnt += 1
#                 continue
#             else:
#                 box[i][j] = j + 1
#
#     for i in range(x, x2 + 1):
#         for j in range(n):
#             if i == x:
#                 if j < y:
#                     continue
#                 else:
#                     r.append(box[i][j])
#                     continue
#             if i == x2:
#                 if j > y2:
#                     continue
#                 else:
#                     r.append(box[i][j])
#                     continue
#             r.append(box[i][j])
#
#     # print(r)
#     # print(r[left:right])
#     # answer = r[left:right+1]
#     # print(r)
#     answer = r
#     return answer
#
# # 1 2 3 4 5
# # 2 2 3 4 5
# # 3 3 3 4 5
# # 4 4 4 4 5
# # 5 5 5 5 5


def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n  # 몫
        b = i % n  # 나머지
        if a < b:
            a, b = b, a
        answer.append(a + 1)

    return answer
