class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        
        for i in range(n):
            l,r = 0,n-1
            while l<=r:
                mat[i][l],mat[i][r] = mat[i][r],mat[i][l]
                l += 1
                r -= 1
        
