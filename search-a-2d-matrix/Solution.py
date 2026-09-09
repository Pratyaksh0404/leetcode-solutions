class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        m, n = len(mat), len(mat[0])
        l, h = 0, m * n - 1

        while l <= h:
            mid = l + (h-l) // 2
            val = mat[mid // n][mid % n]

            if val == tar:
                return True
            elif val < tar:
                l = mid + 1
            else:
                h = mid - 1

        return False