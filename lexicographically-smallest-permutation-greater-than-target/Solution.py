from functools import cache
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        a,b = s,target
        n = len(a)
        c = [0]*26
        
        for i in a:
            c[ord(i)-97] += 1
        t = tuple(c)

        @cache
        def solve(i:int,ct:tuple,g:bool)->str | None:
            if i==n:
                return "" if g else None
            l = list(ct)
            for j in range(26):
                if l[j]>0:
                    if not g and j<ord(b[i])-97:
                        continue
                    ng = g or (j>ord(b[i])-97)
                    l[j] -= 1
                    r = solve(i+1,tuple(l),ng)
                    l[j] += 1
                    if r is not None:
                        return chr(97+j) + r

            return None

        ans = solve(0,t,False)
        return ans or ""
        