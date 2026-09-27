import heapq
class Solution:
    def maxEarnings(self, meet: list[list[int]]) -> int:
        meet.sort()
        h = []
        m = float('-inf')
        ans = 0
        for s,e,r in meet:
            while h and h[0][0]<=s:
                m = max(m,heapq.heappop(h)[1])
            c = r+(s+m if m!=float('-inf') else 0)
            if c>ans:
                ans = c
            heapq.heappush(h,(e,c-e))
        return ans