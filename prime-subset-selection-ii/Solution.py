class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        if n < 2 or s < 2:
            return []
        
        ss = [True] * (n + 1)
        ss[0] = ss[1] = False
        for i in range(2, int(n**0.5) + 1):
            if ss[i]:
                ss[i*i::i] = [False] * len(ss[i*i::i])
        pp = [i for i in range(2, n + 1) if ss[i]]
        
        if not pp or pp[0] > s:
            return []
        
        dp = [None] * (s + 1)
        dp[0] = ()
        
        for p in pp:
            for w in range(s, p - 1, -1):
                if dp[w - p] is not None:
                    cand = dp[w - p] + (p,)
                    if dp[w] is None:
                        dp[w] = cand
                    else:
                        if len(cand) < len(dp[w]) or (len(cand) == len(dp[w]) and cand < dp[w]):
                            dp[w] = cand
        
        maxi = -1
        for w in range(s, -1, -1):
            if dp[w] is not None:
                maxi = w
                break
        
        if maxi <= 0:
            return []
        
        return list(dp[maxi])