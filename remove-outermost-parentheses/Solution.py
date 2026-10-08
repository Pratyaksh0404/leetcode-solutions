class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        f, ans = 0, []

        for i in S:
            if i == ')':
                f -= 1
            if f > 0:
                ans.append(i)
            if i == '(':
                f += 1
        return ''.join(ans)