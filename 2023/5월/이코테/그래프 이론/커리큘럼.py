import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
graph_cost = [[] for i in range(N + 1)]
for i in range(1, N + 1):
    numbers = list(map(int, input().split()))
    cost = numbers[0]
    graph_cost[i] = cost
    for j in range(1, len(numbers) - 1):
        graph[numbers[j]].append(i)
        indegree[i] += 1

graph_sum_cost = [[] for i in range(N + 1)]


def topology_sort():
    result = []
    q = deque()

    # 진입차수 0 인 것 다 넣기.
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append((i, graph_cost[i]))

    while q:
        now, now_cost = q.popleft()
        result.append((now, now_cost))

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append((i, now_cost+graph_cost[i]))

    return result


# print(graph)
# print(graph_cost)
# print(indegree)
answer = topology_sort()
# print(indegree)
answer.sort()

for ans in answer:
    print(ans[1])

