class Solution:
    def findClosestElements(self, nums: list[int], k: int, tar: int) -> list[int]:
        l, r = 0, len(nums) - k
        
        while l < r:
            mid = l + (r - l) // 2
            if tar - nums[mid] > nums[mid + k] - tar:
                l = mid + 1
            else:
                r = mid
                
        return nums[l : l + k]