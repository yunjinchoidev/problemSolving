import math
import time
# import sys
# input = sys.stdin.readline

start_time = time.time()


N = int(input())
answer = 0

quotient, remain = divmod(N, 5)

if remain == 0:
    answer = quotient
elif remain == 1:
    answer = quotient + 2
elif remain == 2 or remain == 4:
    answer = quotient + remain / 2
elif remain == 3:
    answer = quotient + 3

if N == 1 or N == 3:
    answer = -1

# 종료시간
end_time = time.time()
print("WorkingTime: {} sec".format(end_time-start_time))
print(int(answer))
