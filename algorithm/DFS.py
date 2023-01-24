graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()  # 스택 방식. !!
        if n not in visited:
            visited.append(n) # 방문처리
            stack += graph[n] - set(visited)
    return visited

print(DFS(graph_list, root_node))




## 참고
## https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html