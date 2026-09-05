class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])
        
        mx = -1
        for i in range(n):
            if nums[i] > mx: 
                mx = nums[i]
            if mx - suf[i] <= k: 
                return i
        return -1