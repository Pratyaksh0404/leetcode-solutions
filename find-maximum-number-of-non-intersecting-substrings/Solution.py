class Solution:
    def maxSubstrings(self, word: str) -> int:
        ans = 0
        f = {}

        for i, c in enumerate(word):
            if c not in f:
                f[c] = i
            elif i - f[c] + 1 >= 4:
                ans += 1
                f.clear()

        return ans