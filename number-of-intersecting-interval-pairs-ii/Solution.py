from bisect import bisect_right
class Solution:
    def countIntersectingIntervals(self, ii: list[list[int]]) -> int:
        ii.sort(key=lambda x: x[0])
        s = [x[0] for x in ii]
        return sum(bisect_right(s,ii[i][1])-(i+1) for i in range(len(ii)))