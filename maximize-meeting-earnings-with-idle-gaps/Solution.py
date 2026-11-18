from bisect import bisect_right

class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[1])
        
        ends = []
        vals = []
        ans = 0
        maxi = -float('inf')
        
        for s, e, r in meetings:
            idx = bisect_right(ends, s) - 1
            
            c = r + s + vals[idx] if idx >= 0 else r
            
            if c > ans:
                ans = c
                
            new = c - e
            if new > maxi:
                maxi = new
                if ends and ends[-1] == e:
                    vals[-1] = maxi
                else:
                    ends.append(e)
                    vals.append(maxi)
                    
        return ans