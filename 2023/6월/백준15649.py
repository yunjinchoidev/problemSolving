N, M = map(int, input().split())
# print(N, M)


cnt = 0
visited = [False for i in range(N+1)]
result = []
def dfs(my_arr):

    global cnt
    global result
    # print("my_Arr", my_arr)

    if len(my_arr) == M:
        cnt += 1
        result.append(my_arr[:])
        # print(*my_arr)
        return

    for i in range(1, N+1):
        if i not in my_arr:
            visited[i] = True
            my_arr.append(i)
            dfs(my_arr)
            visited[i] = False
            my_arr.pop()

for i in range(1, N+1):
    arr = [i]
    dfs(arr)

# print(cnt)
# print(result)
for i in range(len(result)):
    print(*result[i])