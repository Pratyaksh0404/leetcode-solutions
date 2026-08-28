class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = 0
        for i in nums:
            if ans < 0:
                return False
            elif i > ans:
                ans = i
            ans -= 1
            
        return True