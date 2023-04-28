# # 기존에 풀었던 풀이
# import heapq
# import bisect
#
#
# def solution(play_time, adv_time, logs):
#     answer = ''
#     # print(play_time)
#     # print(adv_time)
#     # print(logs)
#
#     # 시작 시간 순으로 정렬함.
#     logs.sort()
#
#     print(logs)
#
#     def binary_search(start, end, arr, target):
#
#         while start <= end:
#             mid = (start + end) // 2
#
#             if start > end:
#                 return None
#
#             x = 0
#             for i in range(len(arr)):
#                 s, e = arr[i].split('-')
#                 if mid in [s, e]:
#                     x += 1
#
#             if arr[mid] > arr[target]:
#                 start = mid + 1
#             elif arr[mid] < arr[target]:
#                 end = mid - 1
#             else:
#                 return mid
#
#         return None
#
#     # 풀이
#     # 정렬 한번 해주고
#     # 이진 탐색 해주면서 최대가 되는 곳을 찾는다.
#     # 특정 지점에서 최댓 값 X -> 특정 구간에서 최댓 값.
#     # 특정 구간을 찾는다. 그리고 그 구간에서 + playtime 만큼의 find
#     binary_search(0, len(logs) - 1, logs)
#
#     return answer




# 두번 째 풀이

# def solution(play_time, adv_time, logs):
#     answer = ''
#
#     hp, mp, sp = play_time.split(':')
#     int_play_time = 3600 * int(hp) + 60 * int(mp) + int(sp)
#     ha, ma, sa = adv_time.split(':')
#     int_adv_time = 3600 * int(ha) + 60 * int(ma) + int(sa)
#     play_arr = [0 for i in range(int_play_time + 10)]
#
#     # print(len(play_arr))
#
#     def str_to_time(arr, check):
#
#         for log in arr:
#             s, e = log.split('-')
#             h1, m1, s1 = s.split(':')
#             h2, m2, s2 = e.split(':')
#             int_s = 3600 * int(h1) + 60 * int(m1) + int(s1)
#             int_e = 3600 * int(h2) + 60 * int(m2) + int(s2)
#             for i in range(int_s, int_e):
#                 check[i] += 1
#
#     def str_to_time_one(st, check):
#
#         s, e = st.split('-')
#         h1, m1, s1 = s.split(':')
#         h2, m2, s2 = e.split(':')
#         int_s = 3600 * int(h1) + 60 * int(m1) + int(s1)
#         int_e = 3600 * int(h2) + 60 * int(m2) + int(s2)
#
#         return int_s, int_e
#
#     str_to_time(logs, play_arr)
#
#     result = 0
#     u = len(play_arr) - int_adv_time
#     prev = sum(play_arr[:int_adv_time])
#     m = prev
#     for i in range(1, u):
#         s = prev - play_arr[i] + play_arr[i + int_adv_time]
#
#         if s > m:
#             result = i
#             m = s
#
#         prev = s
#
#     print(result)
#     if result == 0:
#         answer = '00:00:00'
#     else:
#
#         result += 1
#         h = result // 3600
#         result %= 3600
#         m = result // 60
#         result %= 60
#         s = result
#
#         if h <= 11:
#             h = '0' + str(h)
#
#         if s < 10:
#             s = '0' + str(s)
#
#         if m < 10:
#             m = '0' + str(m)
#
#         answer = str(h) + ':' + str(m) + ':' + str(s)
#
#     return answer
























