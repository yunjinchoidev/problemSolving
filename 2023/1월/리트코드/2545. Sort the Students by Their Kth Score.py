class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        r = []
        answer = []
        for idx, value in enumerate(score):
            r.append((value[k], idx))

        r.sort(key=lambda x: -x[0])
        # print(r)

        for idx, value in enumerate(r):
            answer.append(score[value[1]])

        return answer
