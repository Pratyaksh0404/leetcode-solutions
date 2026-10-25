class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n:
                return False
            if grid[i][j]:
                return True

            grid[i][j] = 1
            f = True
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if not dfs(r, c):
                    f = False
            return f
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j] and dfs(i, j):
                    ans += 1
        return ans