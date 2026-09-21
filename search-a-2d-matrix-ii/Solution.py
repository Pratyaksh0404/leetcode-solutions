class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        m, n = len(mat) - 1, len(mat[0]) - 1
        
        row, col = m, 0
        while row >= 0 and col <= n:
            curr = mat[row][col]
            if curr == tar:
                return True
            elif curr < tar:
                col += 1 
            else:
                row -= 1  
        return False