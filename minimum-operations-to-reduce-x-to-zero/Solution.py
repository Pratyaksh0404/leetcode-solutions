class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        tar = sum(nums) - x
        if tar == 0:
            return n
        
        ans = curr = 0
        l = 0
        
        for i, j in enumerate(nums):
            curr += j
            while l <= i and curr > tar:
                curr -= nums[l]
                l += 1
            if curr == tar:
                ans = max(ans, i - l + 1)
        
        return n - ans if ans else -1