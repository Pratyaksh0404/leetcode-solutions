class Solution:
    def minRotations(self, s: str) -> int:
        curr = ans = 0
        for i in s:
            t = int(i)
            d = abs(t-curr)
            ans += min(d,10-d)
            curr = t

        return ans