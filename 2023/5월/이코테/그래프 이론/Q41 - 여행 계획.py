import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0] * (N)
graph = [list(map(int, input().split())) for i in range(N)]

numbers = list(map(int, input().split()))

parent = [0] * (N+1)

for i in range(0, N + 1):
    parent[i] = i

# print(parent)
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



for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            union_parent(parent, r+1, c+1)

# print(parent)
answer = "YES"
check_value = parent[numbers[0]]

for i in range(1, len(numbers)):
    if parent[numbers[i]] != check_value:
        answer = 'NO'

print(answer)