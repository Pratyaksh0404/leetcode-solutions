from collections import Counter
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        C = Counter(f for f,_ in items)
        M = {f: sum(C[j] for j in range(f,max(C)+1,f))-1 for f in C}
        mp = min(p for _,p in items)
        ans = 0
        for p,m in sorted((p,M[f]) for f,p in items if M[f]>0 and p<2*mp):
            t = min(m,budget//p)
            ans += t*2
            budget -= t*p

        return ans + budget//mp