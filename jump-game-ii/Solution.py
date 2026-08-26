class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        f = 0

        for i in range(len(nums) - 1):
            f = max(f, i + nums[i])
            if f >= len(nums) - 1:
                ans += 1
                break
            if i == end:      
                ans += 1       
                end = f  

        return ans