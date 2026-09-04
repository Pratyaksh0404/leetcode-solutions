class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def backtrack(r, q, cols, d, ad):
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - c - 1) for c in q])
                return
            
            for c in range(n):
                if c in cols or (r - c) in d or (r + c) in ad:
                    continue
                
                backtrack(r + 1, 
                          q + [c], 
                          cols | {c}, 
                          d | {r - c}, 
                          ad | {r + c})
                
        backtrack(0, [], set(), set(), set())

        return ans