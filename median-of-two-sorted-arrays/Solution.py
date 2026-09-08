class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2) 
        l = len(nums)
        mid = l // 2
        if l % 2 != 0:
            return float(nums[mid])
        else:
            return (nums[mid-1] + nums[mid]) / 2.0