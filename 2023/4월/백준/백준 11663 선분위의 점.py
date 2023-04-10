import sys
import bisect

def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

dots = list(map(int, input().split()))
dots.sort()

def calCountsByRange(nums, left_value, right_value):
    r_i = bisect.bisect_right(nums, right_value)
    l_i = bisect.bisect_left(nums, left_value)
    return r_i - l_i


for i in range(M):

    s, e = map(int, input().split())
    print(calCountsByRange(dots, s, e))
    #
    # print(calCountsByRange(dots, s, e))
    #
    # print(bisect.bisect_right(dots, s))
    # print(bisect.bisect_left(dots, e))
    # length = bisect.bisect_right(s, dots) - bisect.bisect_left(e, dots)
    # print(length)
    #
    #
