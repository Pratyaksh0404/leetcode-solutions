class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans, b = 0, 0
        for i, ch in enumerate(s):
            b = b+1 if ch == '(' else b-1
            if i and s[i-1] + ch == '()':
                ans += 2 ** b
        return ans

