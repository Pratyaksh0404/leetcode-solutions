import math
from functools import reduce
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                s=nums[i:j+1]
                p=math.prod(s)
                lcm=reduce(math.lcm,s)
                gcd=reduce(math.gcd,s)
                if p==lcm*gcd:
                    ans=max(ans,len(s))
        return ans