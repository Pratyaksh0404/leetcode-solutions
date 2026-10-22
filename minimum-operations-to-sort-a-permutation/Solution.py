class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums.index(0)
        if all(i == nums[(start + i) % n] for i in range(n)):
            return min(start, n - start + 2) 
        if all(i == nums[(start - i) % n] for i in range(n)):
            return min(start + 2, n - start)
            
        return -1