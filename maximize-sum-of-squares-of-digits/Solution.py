class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum<1 or sum>9*num:
            return ""
        a = sum
        ans = []
        for i in range(num):
            rem = num-1-i
            flag = False
            for j in range(9,-1,-1):
                if i==0 and j==0 and num>1:
                    continue
                q = a - j
                if q>=0 and q<=9*rem:
                    ans.append(str(j))
                    a -= j
                    flag = True
                    break
            if not flag:
                return ""
        return "".join(ans)