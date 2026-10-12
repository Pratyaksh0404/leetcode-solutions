class Solution:
    def maxPrimeSubset(self, n: int, x: int) -> list[int]:
        ss = [True] * (n+1)
        ss[0]=ss[1]=False
        for i in range(2,int(n**0.5)+1):
            if ss[i]:
                ss[i*i::i] = [False]*len(ss[i*i::i])
        pp = [i for i in range(2,n+1) if ss[i]]
        memo = {}
        def dfs(i,rr):
            if rr<0:
                return None
            if i==len(pp):
                return ()
            if (i,rr) in memo:
                return memo[(i,rr)]
            r1 = dfs(i+1,rr)
            p = pp[i]
            r2 = dfs(i+1,rr-p)
            if r2 is not None:
                r2 = (p,)+r2
            if r1 is None:
                best = r2
            elif r2 is None:
                best = r1
            else:
                s1,s2 = sum(r1),sum(r2)
                best = r1 if s1>s2 else (r2 if s2>s1 else (r1 if len(r1)<len(r2) else (r2 if len(r2)<len(r1) else min(r1,r2))))
            memo[(i,rr)] = best
            return best

        ans = dfs(0,x)
        return list(ans) if ans and sum(ans)>0 else []
        