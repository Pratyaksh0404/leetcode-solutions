class Solution:
    def maxArea(self, h: List[int]) -> int:
        ans = 0
        l, r = 0, len(h) - 1

        while l < r:
            a = min(h[l], h[r]) * (r - l)
            ans = max(ans, a)
            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1
        return ans