from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt


def solution(n, wires):
    answer = n - 2

    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for i in range(n + 1)]
        visited = [False] * (n + 1)
        tmps.pop(i)  # 리스트에서 특정 인덱스를 제거 할 수가 있다. 이걸 못했음.

        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx, g in enumerate(graph):  # 연결 되어 있는 걸을 고르기 위해서 해주는 것임. !!
            if g != []:
                start = idx
                break
        cnt = bfs(graph, start, visited)
        other_cnts = n - cnt  # 자동으로 반대 편이 완성된다는 사실. 음메...
        if abs(cnt - other_cnts) < answer:  ## 갭이 최소 인 것으로 업데이트 해주기
            answer = abs(cnt - other_cnts)
    return answer

