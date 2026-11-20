class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans, f, g = 1, 1, 1
        for i in range(1, n):
            match nums[i] - nums[i - 1]:
                case 2:
                    f, g = g + 1, 1
                    if f > ans: ans = f
                case 1:
                    f, g = max(f + 1, g), g + 1
                    ans = max(ans, f, g)
                case 0:
                    g = max(f + 1, g)
                    if g > ans: ans = g
                case _:
                    f, g = 1, 1
                    
        return ans