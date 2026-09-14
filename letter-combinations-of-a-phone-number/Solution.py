class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz',}

        def solve(idx, comb):
            if idx == len(digits):
                ans.append(comb[:])
                return
            
            for i in dic[digits[idx]]:
                solve(idx + 1, comb + i)

        ans = []
        solve(0, "")

        return ans