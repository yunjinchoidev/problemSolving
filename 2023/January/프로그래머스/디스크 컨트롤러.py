import heapq


def solution(jobs):
    check = []
    answer = 0
    h = []
    jobs.sort()
    print(jobs)
    time = 0
    print(len(jobs))
    visited = [False for i in range(len(jobs))]

    while True:

        hh = []
        for i in range(len(jobs)):
            if jobs[i][0] <= time and visited[i] == False:
                heapq.heappush(hh, (jobs[i][1], jobs[i][0], i))

        if len(hh) == 0:
            time += 1
            continue

        x, y, z = heapq.heappop(hh)
        visited[z] = True
        time += x
        # x = 걸린 시간
        # y = 요청 시간
        # time = 현재 시간
        print(time, x, y, z)
        check.append(time - y)

        if sum(visited) == len(visited):
            break

    answer = int(sum(check) / len(check))

    return answer