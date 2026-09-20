from itertools import combinations

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        return sum(
            a[0] <= b[1] and b[0] <= a[1] 
            for a, b in combinations(intervals, 2)
        )