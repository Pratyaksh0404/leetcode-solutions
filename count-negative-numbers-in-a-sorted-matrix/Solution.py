class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bs(row):
            l, r = 0, len(row)
            while l<r:
                mid = l + (r -l) // 2
                if row[mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            return len(row) - l
        
        ans = 0
        for row in grid:
            ans += bs(row)
        return(ans)

        