class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))
    
        for i in range(len(nums)):
            if digit_sum(nums[i]) == i:
                return i
        return -1