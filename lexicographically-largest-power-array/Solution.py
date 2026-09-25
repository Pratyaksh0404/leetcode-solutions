class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        grp = [nums]
        ans = [0] * 15
        
        for b in range(14, -1, -1):
            mask = 1 << b
            curr = 0
            nxt = []
            f = False
            
            for g in grp:
                if f:
                    nxt.append(g)
                else:
                    s1 = True
                    for x in g:
                        if not (x & mask):
                            s1 = False
                            break
                    
                    if s1:
                        curr += len(g)
                        nxt.append(g)
                    else:
                        f = True
                        gg = [x for x in g if (x & mask)]
                        gw = [x for x in g if not (x & mask)]
                        curr += len(gg)
                        if gg:
                            nxt.append(gg)
                        if gw:
                            nxt.append(gw)
                            
            ans[14 - b] = curr
            grp = nxt
            
        return ans