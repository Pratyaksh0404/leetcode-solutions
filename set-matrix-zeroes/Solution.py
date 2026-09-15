class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        rows, cols = len(mat), len(mat[0])
        zr = set()
        zc = set()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    zr.add(r)
                    zc.add(c)
        
        for r in zr:
            mat[r] = [0] * cols
            
        for c in zc:
            for r in range(rows):
                mat[r][c] = 0