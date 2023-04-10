import sys
from pprint import pprint


def input():
    return sys.stdin.readline().rstrip()


K, N, F = map(int, input().split())

# 1. 소풍에 갈 수 있는 학생들의 번호를 입력받는다.
friends_adjascent = [[] for _ in range(N+1)]

input_friends = set()

for _ in range(F):
    s, e = map(int, input().split())
    friends_adjascent[s].append(e)
    friends_adjascent[e].append(s)
    input_friends.add(s)

def dfs(v, arr):
    if len(arr) == K:
        for a in arr:
            print(a)
        sys.exit(0)

    for i in range(v + 1, N + 1):
        if not visited[i]:
            for num in arr:
                if num not in friends_adjascent[i]:
                    break
            else:
                visited[i] = True
                dfs(i, arr + [i])

for friend in input_friends:
    visited = [False for _ in range(N+1)]
    visited[friend] = True
    dfs(friend, [friend])

print(-1)
