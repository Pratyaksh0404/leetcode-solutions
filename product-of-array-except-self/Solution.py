class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n

        pre = 1
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]

        su = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= su
            su *= nums[i]

        return ans