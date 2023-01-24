# 풀이코드
# 여기에 풀이코드를 복사 붙여넣기 해주세요
# 주석은 굳이 지울 필요없이 팀원들이 이해하기 좋은 방식의 코드를 붙여넣기 해주세요 ~!


## 프림알고리즘으로 푼 풀이
import heapq
from collections import defaultdict


def solution(n, costs):
    answer = 0

    cost2 = []
    for i in range(len(costs)):  ## 인접행렬 만들기
        cost2.append((costs[i][2], str(costs[i][0]), str(costs[i][1])))

    # print(cost2)
    def prim(start_node, edges):
        mst = list()
        adjacent_edges = defaultdict(list)
        for weight, n1, n2 in edges:
            adjacent_edges[n1].append((weight, n1, n2))
            adjacent_edges[n2].append((weight, n2, n1))

        connected_nodes = set(start_node)
        candidate_edge_list = adjacent_edges[start_node]
        heapq.heapify(candidate_edge_list)
        while candidate_edge_list:

            weight, n1, n2 = heapq.heappop(candidate_edge_list)
            if n2 not in connected_nodes:  ## 아직 방문 안한 것만
                connected_nodes.add(n2)
                mst.append((weight, n1, n2))  ## 힙이니깐 최소가 나온게 당연하므로 그냥 붙이면 된다.

                for edge in adjacent_edges[n2]:
                    if edge[2] not in connected_nodes:  ## 방문하지 않은 것들을 다시 힙에 넣어줌!
                        heapq.heappush(candidate_edge_list, edge)

        return mst

    mm = prim('0', cost2)
    for i in mm:
        answer += i[0]

    return answer


# 크루스칼 알고리즘 으로 푼다면 ?
def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    print(parent)

    def find(p, x):  ## 부모 노드 찾기
        if p[x] != x:
            p[x] = find(p, p[x])
        return p[x]

    def union(p, x, y):  ## 합치기
        x = find(p, x)
        y = find(p, y)
        if x < y:
            p[y] = x
        else:
            p[x] = y

    cost2 = []
    for i in range(len(costs)):  ## 인접행렬 만들기
        cost2.append((costs[i][2], costs[i][0], costs[i][1]))

    cost2.sort()
    # print(cost2)
    total_cost = 0
    for i in range(len(cost2)):  ## 순회
        mst = []
        w, l, r = cost2[i]
        # print(w, l, r, parent)
        if find(parent, l) != find(parent, r):  ## 부모가 다를때 합친다. 같으면 합치면 안됨
            # print(w, l, r)
            union(parent, l, r)
            total_cost += w

    answer = total_cost
    return answer