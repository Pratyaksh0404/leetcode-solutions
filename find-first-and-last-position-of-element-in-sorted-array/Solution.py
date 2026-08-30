class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def solve(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid               
            return lo
        
        lo = solve(target)
        hi = solve(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]