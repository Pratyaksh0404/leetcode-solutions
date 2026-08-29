class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        l,r = 0,len(nums)-1
        
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==tar:
                return mid
            elif nums[mid]>tar:
                r = mid-1
            else:
                l = mid+1
        
        return -1