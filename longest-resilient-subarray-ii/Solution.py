import math
class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        ans = i = 0
        n = len(nums)
        while i<n:
            r = nums[i]%k
            j = i
            while j< n and nums[j]%k==r:
                j += 1
            t = j-i
            ans = max(ans,t if r==0 else 1+((t-1)//(k//math.gcd(r,k)))*(k//math.gcd(r,k)))

            i = j

        return ans