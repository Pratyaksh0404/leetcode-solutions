from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        tot = sum(nums)
        return len(nums)*maxi-tot