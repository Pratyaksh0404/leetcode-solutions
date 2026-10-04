class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        d00 = d01 = d10 = d11 = ans = -10**20
        
        for i in nums:
            d00, d01, d10, d11 = (
                d01 + i if d01 > 0 else i,
                d00 - i,
                d00 if d00 > d11 + i else d11 + i,
                d01 if d01 > d10 - i else d10 - i
            )
            
            if d00 > ans: 
                ans = d00
            if d01 > ans: 
                ans = d01
            if d10 > ans: 
                ans = d10
            if d11 > ans: 
                ans = d11
            
        return ans