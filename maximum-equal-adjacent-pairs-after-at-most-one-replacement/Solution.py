from itertools import pairwise
from collections import defaultdict

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:        
        q = 0
        g = defaultdict(int)
        
        for a, b in pairwise(nums):
            if a == b:
                q += 1
            else:
                if a > b:
                    a, b = b, a
                g[(a, b)] += 1
                
        return q + max(g.values(), default=0)