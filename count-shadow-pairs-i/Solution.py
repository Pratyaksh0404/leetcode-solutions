import bisect

class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        v = nums  
        n = len(v)
        
        sval = sorted(set(v))
        c = [bisect.bisect_left(sval, x) for x in v]
        
        r, stk = [n] * n, []
        for i, x in enumerate(v):
            while stk and v[stk[-1]] > x:
                r[stk.pop()] = i
            stk.append(i)
            
        last = [n] * len(sval)
        cnt = [0] * n
        ans = 0
        
        for i in range(n - 1, -1, -1):
            a = c[i]
            nxt = last[a]
            cnt[i] = 1 + (cnt[nxt] if nxt < r[i] else 0)
            last[a] = i
            ans += r[i] - i - cnt[i]
            
        return ans