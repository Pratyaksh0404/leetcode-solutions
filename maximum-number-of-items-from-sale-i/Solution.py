class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        dp,F = [0]+[-1]*budget, [i for i,_ in items]
        for f,p in items:
            v = sum(1 for x in F if x%f==0)
            for w in range(budget,p-1,-1):
                if dp[w-p]>-1:
                    dp[w]=max(dp[w],dp[w-p]+v)
        m=min(p for _,p in items)
        
        return max(v+(budget-w)//m for w,v in enumerate(dp) if v>-1)