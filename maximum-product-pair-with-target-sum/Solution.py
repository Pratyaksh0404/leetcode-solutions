class Solution:
    def maxProductPair(self, nums: list[int], tar: int) -> list[int]:
        ans = [-1,-1]
        maxi = -float('inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==tar and nums[i]>nums[j]:
                    p = nums[i]*nums[j]
                    if p>maxi:
                        maxi = p
                        ans = [i,j]

        return ans