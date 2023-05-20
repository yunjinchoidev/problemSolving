import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    cnt = 0
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        cnt += 1
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        z = x + 2 * y
        heapq.heappush(scoville, z)

    answer = cnt

    if len(scoville) == 1:
        c = heapq.heappop(scoville)
        if c < K:
            answer = -1

    return answer
