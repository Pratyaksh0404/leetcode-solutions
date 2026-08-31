class Solution:
    def longestPalindrome(self, s: str) -> int:
        cs = set()
        ans = 0
        for i in s:
            if i in cs:
                cs.remove(i)
                ans += 2
            else:
                cs.add(i)
        if cs:
            ans += 1
        return ans