class Solution:
    def dfs(self, grid: List[List[str]], row: int, col: int, R: int, C: int):
        diff = [0,1,0,-1,0]
        grid[row][col] = '0'
        
        for di in range(4):
            adjR, adjC = row+diff[di], col+diff[di+1]
            if(adjR >= 0 and adjR < R and adjC >= 0 and adjC < C and grid[adjR][adjC] == '1'):
                self.dfs(grid,adjR,adjC,R,C)

    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0

        for r in range(R):
            for c in range(C):
                if(grid[r][c] == '1'):
                    self.dfs(grid,r,c,R,C)
                    ans+=1
        return ans