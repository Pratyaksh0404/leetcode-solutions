class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s = sorted((interval[0], i) for i, interval in enumerate(intervals))
        n = len(intervals)
        ans = []

        for _, end in intervals:
            left, right = 0, n - 1
            ind = -1

            while left <= right:
                mid = (left + right) // 2
                if s[mid][0] >= end:
                    ind = s[mid][1]  
                    right = mid - 1 
                else:
                    left = mid + 1 

            ans.append(ind)

        return ans