class Solution:
    def reverseDegree(self, s: str) -> int:

        ans, i = 0, 1
        for ch in s:
            ans += (123 - ord(ch)) * i
            i += 1

        return ans    