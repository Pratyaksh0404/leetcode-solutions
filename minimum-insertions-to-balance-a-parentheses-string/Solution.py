class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        bal = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == ')':
                if i+1 <len(s) and s[i+1] == ')':
                    if bal > 0:
                        bal -=1 
                    else:
                        ans += 1
                    i+=1
                elif bal > 0:
                    ans += 1
                    bal -=1 
                else:
                    ans += 2
            else:
                bal += 1
            i+=1
        return ans + bal * 2   


