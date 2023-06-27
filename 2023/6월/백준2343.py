N, M = map(int, input().split())

numbers = list(map(int, input().split()))
# print(N, M, numbers)

lo = -1
hi = int(1e9)


# print(lo, hi)

def check(arr, muge):
    # 크기

    global M

    current_weight = 0
    cnt = 1
    for i in range(len(arr)):
        # x +=
        if current_weight + arr[i] > muge:
            current_weight = arr[i]
            cnt += 1
        else:
            current_weight += arr[i]

        if cnt > M:
            return False

    return True


lo = max(numbers)
hi = sum(numbers)

while lo < hi:

    # CD 최소 크기 mid
    mid = (lo + hi) // 2
    # print(mid)

    # 가능하다면 줄여야지
    if check(numbers, mid):
        hi = mid-1
    else:
        # 불가능하면 늘린다.
        lo = mid+1


print(hi)
