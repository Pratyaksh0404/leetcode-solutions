class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        if k != 0:
            arr = nums[n-k:]
            del nums[n-k:]
            nums[0:0] = arr
 