import sys
import time
import heapq

input = sys.stdin.readline

start_time = time.time()

N = int(input())
time_table = []
h = []

# 힙을 이용해 시작 시간, 종료시간을 저장한다.
for i in range(N):
    s, e = list(map(int, input().split()))
    heapq.heappush(h, (s, e))

lectureing = []
max_lecture_cnt = 0

# max_lecture_cnt += 1
# heapq.heappush(lectureing, h[0][1])
# heapq.heappop(h)

while True:

    if not h :
        break

    if lectureing:
        min_end = lectureing[0]

        input_s, input_e = h[0]
        if input_s < min_end:
            if len(lectureing) >= max_lecture_cnt:
                max_lecture_cnt += 1

            heapq.heappush(lectureing, h[0][1])
            heapq.heappop(h)
        else:
            # lectureing = []
            heapq.heappop(lectureing)
            # heapq.heappop(h)
    else:
        max_lecture_cnt += 1
        heapq.heappush(lectureing, h[0][1])
        heapq.heappop(h)


# print(h)

print(max_lecture_cnt)


end_time = time.time()
print("WorkingTime: {} sec".format(end_time - start_time))
