import sys
from collections import deque

# input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    m = int(input())
    changes = [list(map(int, input().split())) for i in range(m)]

    adj = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(len(numbers) - 1):
        adj[numbers[i]].append(numbers[i + 1])
        indegree[numbers[i]] += 1
    print(indegree)

    for i in range(len(changes)):

        if changes[i][0] in adj[changes[i][1]]:
            adj[changes[i][1]].remove(changes[i][0])
            adj[changes[i][1]].append(numbers[i][1])
            indegree[changes[i][1]] -= 1

        adj[changes[i][0]].append(changes[i][1])
        indegree[changes[i][0]] += 1

    result = []
    q = deque()

    print(indegree)
    # 진입차수 0 인 것 다 넣기.
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)  # result 에 넣어주기

        for i in adj[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)  # 시간 더해서 넣어주기

    print(result)
