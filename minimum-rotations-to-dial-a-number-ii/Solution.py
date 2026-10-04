class Solution:
    def minRotations(self, n: int, s: str) -> int:
        dig = [int(c) for c in s]
        pre = [0]*n
        curr = 0
        for i in range(n):
            d = abs(dig[i]-curr)
            pre[i] = (pre[i-1] if i>0 else 0) + min(d,10-d)
            curr = dig[i]

        rev = [0]*(n+1)
        for i in range(n-2,-1,-1):
            d = abs(dig[i]-dig[i+1])
            rev[i] = rev[i+1]+min(d,10-d)

        ans = pre[-1]
        for k in range(n):
            if k==0:
                cost = min(dig[-1],10-dig[-1])
            else:
                cost = pre[k-1]
                d = abs(dig[-1]-dig[k-1])
                cost += min(d,10-d)
            cost += rev[k]
            ans = min(ans,cost)

        return ans
                