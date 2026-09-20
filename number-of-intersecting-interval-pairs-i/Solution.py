class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        return sum(a[0]<=b[1] and b[0]<=a[1] for i,a in enumerate(intervals) for b in intervals[i+1:])