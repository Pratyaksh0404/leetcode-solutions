class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        inf = float('inf')
        d00 = d01 = d10 = d11 = -inf
        ans = -inf
        for i in nums:
            n00 = max(i,d01+i)
            n01 = d00-i
            n10 = max(d11+i,d00)
            n11 = max(d10-i,d01)

            d00,d01,d10,d11 = n00,n01,n10,n11
            ans = max(ans,d00,d01,d10,d11)

        return ans