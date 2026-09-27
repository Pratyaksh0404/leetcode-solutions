from collections import Counter
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        q = 0
        g = Counter()
        for a,b in zip(nums,nums[1:]):
            if a==b:
                q += 1
            else:
                g[(a,b) if a<b else (b,a)]+=1
        return q + (max(g.values()) if g else 0)