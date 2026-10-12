class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n<2:
            return []
        ss = [True]*(n+1)
        ss[0] = ss[1] = False
        for i in range(2,int(n**0.5)+1):
            if ss[i]:
                for j in range(i*i,n+1,i):
                    ss[j] = False
        pp = [i for i in range(2,n+1) if ss[i]]
        ans = []
        x = 0
        for i in pp:
            if x+i<=s:
                x+=i
                ans.append(i)
            else:
                break
        return ans