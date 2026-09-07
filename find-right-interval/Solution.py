import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s = sorted((inter[0], i) for i, inter in enumerate(intervals))
        n = len(s)
        
        return [
            s[idx][1] if (idx := bisect.bisect_left(s, (end,))) < n else -1 
            for _, end in intervals
        ]