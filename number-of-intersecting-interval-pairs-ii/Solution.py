from bisect import bisect_right

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        a = intervals
        a.sort(key=lambda x: x[0])
        s = [x[0] for x in a]
        
        return sum(
            bisect_right(s, end) - (i + 1) 
            for i, (_, end) in enumerate(a)
        )