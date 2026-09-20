class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        ans = 0
        n = len(intervals)
        for i in range(n):
            a_start, a_end = intervals[i]
            for j in range(i + 1, n):
                b_start, b_end = intervals[j]
                if a_start <= b_end and b_start <= a_end:
                    ans += 1
                    
        return ans