class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans = -1
        for i, s in enumerate(list(accumulate(nums[::-1], min))[::-1]):
            ans = max(ans, nums[i])
            if ans - s <= k: 
                return i
        return -1
