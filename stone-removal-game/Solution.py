class Solution:
    def canAliceWin(self, n: int) -> bool:
        k = 10
        ans = False
        while n >= k:
            n -= k
            k -= 1
            ans = not ans
        return ans