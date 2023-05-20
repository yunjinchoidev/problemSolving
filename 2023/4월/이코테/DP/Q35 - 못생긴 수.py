class Solution:
    def isUgly(self, n: int) -> bool:
        flag = False
        cnt = 1
        print(n)
        if n == 0:
            return False
        while cnt != 0:
            cnt = 0

            if n % 2 == 0:
                n /= 2
                cnt += 1
            elif n % 3 == 0:
                n /= 3
                cnt += 1
            elif n % 5 == 0:
                n /= 5
                cnt += 1

            if n == 1:
                flag = True
                break

        return flag
