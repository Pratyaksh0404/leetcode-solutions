class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a = 0
        ans = 0

        for c in s:
            if c == '(':
                a += 1
            else:
                if a > 0:
                    a -= 1
                else:
                    ans += 1

        return ans + a