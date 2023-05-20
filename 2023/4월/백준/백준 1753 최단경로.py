import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))


V, E = map(int, input().split())
start = int(input())
INF = 10**9
dis = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dijkstra(start)
for n in dis[1:]:
    print(n if n != INF else "INF")
