class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        q = sorted([abs(x) for x in nums])
        neg = sum(x**2 for x in q[:n//2])
        pos = sum(x**2 for x in q[n//2:])

        return pos-neg