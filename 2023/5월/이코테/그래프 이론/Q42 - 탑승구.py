import sys

input = sys.stdin.readline
G = int(input())
P = int(input())

numbers = []
for i in range(P):
    numbers.append(int(input()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (G + 1)
for i in range(0, G + 1):
    parent[i] = i

answer = 0
num_cnt_list = [0] * (G + 1)
for i in range(P):
    input_number = numbers[i]
    if set(parent[1:input_number + 1]) == set([0]):
        break
    else:
        union_parent(parent, input_number-num_cnt_list[input_number], 0)
        answer += 1
        num_cnt_list[input_number] += 1
print(answer)















#
# import sys
#
# input = sys.stdin.readline
# G = int(input())
# P = int(input())
#
# numbers = []
# for i in range(P):
#     numbers.append(int(input()))
#
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# # 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     # parent[a] = 0
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# parent = [0] * (G + 1)
# for i in range(0, G + 1):
#     parent[i] = i
#
# answer = 0
# # num_cnt_list = [0] * (G + 1)
# for i in range(P):
#     input_number = find_parent(parent, numbers[i])
#     # print(parent)
#     # print(parent[1:input_number + 1].count(0))
#
#     # if set(parent[1:input_number + 1]) == set([0]):
#     #     break
#     # else:
#     if input_number == 0:
#         break
#         # parent[input_number-num_cnt_list[input_number]] = 0
#         # union_parent(parent, input_number-num_cnt_list[input_number])
#     union_parent(parent, input_number, input_number - 1)
#     # parent[find_parent(parent, input_number-num_cnt_list[input_number])] = 0
#     # union_parent(parent, input_number-num_cnt_list[input_number], 0)
#     answer += 1
#     # num_cnt_list[input_number] += 1
# print(answer)
#
#
#
#
