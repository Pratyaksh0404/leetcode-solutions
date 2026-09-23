class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        l = height[0]
        add = 0
        j = len(height) - 1
        r = height[j]
        while i < j:
            if l <= r:
                add += l - height[i]
                i += 1
                l = max(l, height[i])
            else:
                add += r - height[j]
                j -= 1
                r = max(r, height[j])
        return add