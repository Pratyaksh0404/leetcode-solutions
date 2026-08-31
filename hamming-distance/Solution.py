class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = x ^ y
        ans = 0
        while d:
            d = d & (d - 1)
            ans += 1
        return ans