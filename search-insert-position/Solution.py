class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while right >= left:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


 