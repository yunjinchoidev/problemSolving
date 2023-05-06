from copy import deepcopy

N = int(input())
H = list(map(int, input().split()))
# 수열을 s에 그대로 카피한다
S = deepcopy(H)
result = 0

for i in range(1, N):
    S[i] += S[i - 1]

for i in range(1, N - 1):  # 오른쪽
    # 마지막값 (전체 누적값)에서 벌 위치 두개를 빼주고,
    # 벌 한마리는 i이후부터 시작함으로 그 이전 값을 빼준것
    result = max(result, 2 * S[-1] - H[0] - H[i] - S[i])

for i in range(1, N - 1):  # 왼쪽
    # 이번에는 두배를 하는게 아니라 따로 더해줘야 함
    # 첫번째 벌: S[-1]-H[-1]-H[i]
    # 두번째 벌: S[i-1]
    result = max(result, S[-1] - H[-1] - H[i] + S[i - 1])
for i in range(1, N - 1):  # 중간
    # i는 꿀의 위치이다.
    # 첫번째벌은 꿀까지의 누적합에서 자기 위치를 빼준다.
    # 두번째벌은 전체 누적합에서 꿀까지의 누적합을 빼주고 자기 위치를 뺴준다.
    result = max(result, S[i] - H[0] + S[-1] - S[i - 1] - H[-1])

print(result)