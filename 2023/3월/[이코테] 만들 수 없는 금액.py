N = int(input())
numbers = list(map(int, input().split()))
visited = [False for i in range(1000000)]


def DFS(n):
    stack = []
    stack.append(n)
    visited[n] = True

    while stack:
        stack.pop(0)
        y = numbers.pop()
        stack.append(y)
        visited[n + y] = True
        DFS(y)
        stack.pop(0)
        numbers.append(y)


DFS(numbers[0])

for i in range(len(visited)):
    if not visited[i]:
        print(i)

