import heapq


def solution(operations):
    answer = []
    h = []

    for i in operations:
        x = i.split(" ")[0]
        y = int(i.split(" ")[1])

        if x == 'I':
            heapq.heappush(h, y)
        elif x == 'D':

            if len(h) == 0:
                continue

            if y == 1:
                h = heapq.nlargest(len(h), h)[1:]
                heapq.heapify(h)
            else:
                k = heapq.heappop(h)

    if h:
        answer.append(max(h))
        answer.append(min(h))
    else:
        answer.append(0)
        answer.append(0)

    return answer
