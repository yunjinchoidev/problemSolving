from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

visited = [False for i in range(N + 1)]

adj = [[] for i in range(N + 1)]

for i in range(M):
    s, e = map(int, input().split())
    adj[s].append((e))


def BFS(s, distance):
    d = deque()
    d.append((s, distance))
    visited[s] = True
    result = []

    while d:
        x, dis = d.popleft()

        if dis == K:
            result.append(x)

        if dis > K:
            return result

        for p in adj[x]:
            if not visited[p]:
                d.append((p, dis + 1))
                visited[p] = True

    return result


result = BFS(X,0)
result.sort()
if len(result) > 0 :
    for r in result:
        print(r)
else:
    print(-1)