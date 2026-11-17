class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        @cache
        def subpalin(i,j):
            l = j-i+1
            st = s[i:j+1]
            if l < 2: return inf
            res = inf
            for p in range(1,l//2+1):
                if l % p == 0:
                    d = l // p
                    subres = 0
                    for ii in range(p):
                        sub = st[ii::p]
                        for jj in range(d//2):
                            if sub[jj]!=sub[d-1-jj]:
                                subres += 1
                    res = min(subres,res)
            return res
        N = len(s)
        @cache
        def dp(i,r):
            if i == N and r == 0:
                return 0
            if i == N:return inf
            res = inf
            for j in range(i+1,N):
                res = min(res,subpalin(i,j)+dp(j+1,r-1))
            return res
        return dp(0,k)



        