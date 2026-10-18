class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        p,k = -1,0
        for i in nums:
            if i!=p:
                p,k = i,k+1
        return len(nums)-k