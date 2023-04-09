K, N = map(int, input().split())
lines = [int(input()) for i in range(K)]
lines.sort()


def binary_search(start, end, lines, N):
    while start <= end:
        mid = (start + end) // 2
        s = 0
        for line in lines:
            s += line // mid

        if s >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end


print(binary_search(1, lines[-1], lines, N))
