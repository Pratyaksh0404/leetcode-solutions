class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        c = [0]*32768
        for x in nums:
            c[x] += 1
        for i in range(15):
            for m in range(32768):
                if not (m & (1<<i)):
                    c[m] += c[m | (1<<i)]
        p = [0]*15

        def check(p):
            for v in set(p) | {len(nums)}:
                if v and c[sum(1<<j for j in range(15) if p[14-j]>=v)] < v:
                    return False
            return True

        for b in range(14,-1,-1):
            i,l,h,r = 14-b,0,len(nums),0
            while l<=h:
                m = (l+h)//2
                p[i] = m
                if check(p):
                    r,l = m,m+1
                else:
                    h = m-1
            p[i] = r
        return p

