class Solution:
    def maxValue(self, nums: List[int]) -> int:
        p = tot = m = 0
        mx = [0,-float('inf')]
        for i,x in enumerate(nums):
            v = x if i%2==0 else -x
            tot += v
            p += v
            j = 1-(i%2)
            if p-mx[j]<m:
                m = p-mx[j]
            if p>mx[j]:
                mx[j] = p
        return tot - 2*m