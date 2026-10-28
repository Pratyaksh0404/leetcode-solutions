class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dp = [set() for _ in range(m)]
        dp[0].add(grid[0][0])

        for i in range(1,m):
            v = grid[0][i]
            for j in dp[i-1]:
                dp[i].add(j^v)

        for i in range(1,n):
            new = [set() for _ in range(m)]
            for j in range(m):
                v = grid[i][j]
                if j>0:
                    for k in new[j-1]:
                        new[j].add(k^v)

                for k in dp[j]:
                    new[j].add(k^v)
            dp = new

        return min(dp[m-1])