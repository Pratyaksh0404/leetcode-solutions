class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        shift = []
        for i in range(n):
            k = rowShift[i] % n
            shift.append(grid[i][k:] + grid[i][:k])
            
        ans = [[0] * n for _ in range(n)]
        for j in range(n):
            k = colShift[j] % n
            for i in range(n):
                row = (i + k) % n
                ans[i][j] = shift[row][j]
                
        return ans