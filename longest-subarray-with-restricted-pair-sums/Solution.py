class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if n-i<=ans:
                break
            seen = 0
            pp = 0
            for j in range(i,n):
                v = nums[j]
                if (pp>>v) & 1 or (seen & (seen>>v)):
                    if j-i>ans:
                        ans = j-i
                    break
                pp |= (seen << v)
                seen |= (1<<v)
            else:
                if n-i > ans:
                    ans = n-i
        return ans