class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l, r  

        ans = 1
        for i in range(n):
            for l0, r0 in ((i, i), (i, i + 1)):
                l, r = expand(l0, r0)
                ans = max(ans, r - l)  

                l1, r1 = expand(l - 1, r)
                ans = max(ans, r1 - l1 - 1)

                l2, r2 = expand(l, r + 1)
                ans = max(ans, r2 - l2 - 1)
                
                if ans >= n:
                    return n

        return ans