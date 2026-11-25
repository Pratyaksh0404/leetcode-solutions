class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l,h = 1,n
        ans = n
        MOD = 10**18 + 9
        base = 1000003
        def check(L):
            count = {}
            curr = 0
            for i in range(L):
                curr = (curr*base+nums[i])%MOD
            count[curr] = count.get(curr,0)+1

            pp = pow(base,L-1,MOD)

            for i in range(L,n):
                curr = (curr-nums[i-L]*pp)%MOD
                curr = (curr*base + nums[i])%MOD
                count[curr] = count.get(curr,0)+1

            for c in count.values():
                if c==1:
                    return True
            return False

        while l<=h:
            mid = (l+h)//2
            if check(mid):
                ans = mid
                h = mid-1
            else:
                l = mid+1

        return ans









            