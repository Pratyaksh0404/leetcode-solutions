class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        ans = 0
        while diff:
            diff = diff & (diff - 1)
            ans += 1
        return ans