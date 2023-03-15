def solution(food_times, k):
    answer = 0
    l = len(food_times)
    repeat = 0

    if k < len(food_times):
        return k + 1

    while True:
        if k < l * min(food_times):
            break

        k -= l * min(food_times)
        idx = food_times.index(min(food_times))
        food_times[idx] = float("inf")  # 무한대로 바꿈.
        l -= 1
        repeat += 1

        if k >= l:
            break

    # print(repeat)
    # print(food_times, k)

    for i in range(len(food_times)):
        food_times[i] -= repeat

    check_idx = 0
    while True:
        if food_times[check_idx] == float("inf") or food_times[check_idx] == 0:
            check_idx += 1
            check_idx %= len(food_times)
            continue
        else:
            k -= 1
            food_times[check_idx] -= 1
            check_idx += 1

            if k != -1:
                check_idx %= len(food_times)

            # print(food_times, idx, check_idx, k)
            if k == -1:
                return check_idx

