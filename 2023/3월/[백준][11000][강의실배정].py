import sys
import time

input = sys.stdin.readline

start_time = time.time()

N = int(input())
time_table = []
for i in range(N):
    time_table.append(list(map(int, input().split())))

print(time_table)

end_time = time.time()
print("WorkingTime: {} sec".format(end_time - start_time))
