class Solution:
    def successfulPairs(self, s1, p, s):
        p.sort()
        m = len(p)
        ans = []
        for i in s1:
            l, r = 0, m - 1
            ii = -1
            while l <= r:
                mid = (l + r) // 2
                if i * p[mid] >= s:
                    ii = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            ans.append(0 if ii == -1 else m - ii)
        
        return ans