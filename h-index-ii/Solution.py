class Solution:
    def hIndex(self, c: List[int]) -> int:
        n = len(c)
        l, r = 0, n
        while l < r:
            mid = l + (r-l) // 2
            if c[mid] >= (n - mid):
                r = mid
            else:
                l = mid + 1
        return n - r