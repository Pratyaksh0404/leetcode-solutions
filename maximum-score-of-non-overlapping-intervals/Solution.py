class Solution:
    def maximumWeight(self, inti: List[List[int]]) -> List[int]:
        n = len(inti)
        si = sorted(
            [(inti[i][0], inti[i][1], inti[i][2], i) for i in range(n)],
            key=lambda x: x[1]
        )
        
        rights = [item[1] for item in si]
        
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]
        
        for i in range(1, n + 1):
            l, r, w, idx = si[i - 1]
            j = bisect_left(rights, l)
            
            for k in range(1, 5):
                dp[k][i] = dp[k][i - 1]
                
                pw, pi = dp[k - 1][j]
                cw = pw + w
                ci = sorted(pi + [idx])
                
                if cw > dp[k][i][0]:
                    dp[k][i] = (cw, ci)
                elif cw == dp[k][i][0]:
                    if ci < dp[k][i][1]:
                        dp[k][i] = (cw, ci)
                        
        ww = -1
        ii = []
        
        for k in range(1, 5):
            w, ind = dp[k][n]
            if w > ww:
                ww = w
                ii = ind
            elif w == ww:
                if ind < ii:
                    ii = ind
                    
        return ii