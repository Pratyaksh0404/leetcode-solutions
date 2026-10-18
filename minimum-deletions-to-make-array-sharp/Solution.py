class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        return sum(a == b for a, b in zip(nums, nums[1:]))
