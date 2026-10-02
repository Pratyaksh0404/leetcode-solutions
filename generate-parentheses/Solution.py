class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def dfs(open, close, s):
            if open == close and open + close == 2*n:
                ans.append(s)
                return
            
            if open < n:
                dfs(open + 1, close, s + "(")
            
            if close < open:
                dfs(open, close + 1, s + ")")

        dfs(0, 0, "")
        return ans