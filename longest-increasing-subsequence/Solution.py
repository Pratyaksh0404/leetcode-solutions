from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ans = []
        for i in nums:
            idx = bisect_left(ans, i)
            
            if idx == len(ans):
                ans.append(i)
            else:
                ans[idx] = i
                
        return len(ans)