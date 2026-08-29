class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        ans = 0
        for i in range(len(s)):
            curr = r[s[i]]
            nxt = r[s[i+1]] if i+1 < len(s) else 0
            
            if curr < nxt:
                ans -= curr
            else:
                ans += curr
        
        return ans