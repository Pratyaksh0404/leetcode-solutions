class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a = nums.index(min(nums))
        b = nums.index(max(nums))
        if b<a:
            a, b = b, a
        n = len(nums)

        return min((a+1) + (n-b), b+1, n-a)