import itertools
import copy

N = int(input())

map_ = [list(map(str, input().split())) for i in range(N)]

coords = [(r, c) for c in range(N) for r in range(N) if map_[r][c] == 'X']
combis = list(itertools.combinations(coords, 3))

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def DFS(row, col, map_):

    visited = [[False for c in range(N)] for r in range(N)]
    stack = []
    stack.append((row, col))
    visited[row][col] = True

    while stack:
        r, c = stack.pop()

        # 디렉션
        for i in range(4):

            # 뎁스가 계속 들어가는 것임.
            for dep in range(1, N + 1):

                nr = r + dr[i] * dep
                nc = c + dc[i] * dep

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                # 해당 방향에 장애물이 존재하면 해당 방향으로 더 이상 감시 불가
                if map_[nr][nc] == 'O':
                    break

                # 학생 감시 성공
                if map_[nr][nc] == 'S':
                    return False

                # 방문 표시
                if not visited[nr][nc]:
                    visited[nr][nc] = True

    return True


# 브루트 포스
for comb in combis:

    # 장애물을 설치
    copy_map_ = copy.deepcopy(map_)
    copy_map_[comb[0][0]][comb[0][1]] = 'O'
    copy_map_[comb[1][0]][comb[1][1]] = 'O'
    copy_map_[comb[2][0]][comb[2][1]] = 'O'

    answer = 'YES'

    # 맵 내의 모든 선생님들이 감시할 수 있는 범위를 DFS 를 통해 조사.
    for r in range(N):
        for c in range(N):
            if copy_map_[r][c] == 'T':
                if not DFS(r, c, copy_map_):
                    answer = 'NO'
        if answer == 'NO':
            break

    # 어떤 장애물의 조합이 모든 선생님들이 단 한번도 감시를 성공하지 못한 경우가 발생한 경우.
    if answer == 'YES':
        break

print(answer)
