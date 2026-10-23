class Solution:
    def numTrees(self, n: int) -> int:
        ans = {0:1, 1:1}

        for i in range(2, n+1):
            t = 0

            for j in range(i):
                t += ans[j]*ans[i-j-1]

            ans[i] = t

        return ans[n]
        