class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        return sum(
            nums.index(x) + nums.count(x) - 1 == len(nums) - 1 - nums[::-1].index(x)
            for x in set(nums)
        )