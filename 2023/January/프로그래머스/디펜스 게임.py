import heapq


def solution(n, k, enemy):
    answer = 0
    h = []
    heapq.heapify(h)
    i = 0
    while True:
        if i >= len(enemy):
            break
        if n - enemy[i] > 0:
            n -= enemy[i]
            heapq.heappush(h, -1 * enemy[i])
            answer += 1
            i += 1
        else:
            if k > 0:
                k -= 1
                n -= enemy[i]
                heapq.heappush(h, -1 * enemy[i])
                n += -1 * heapq.heappop(h)
                i += 1
                answer += 1
                if i == len(enemy):
                    break
                continue
            else:
                break
    return answer


print(solution(2, 4, [1, 1, 1, 2]))
