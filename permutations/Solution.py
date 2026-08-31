class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        per = []
        pick = [False]*len(nums)
        
        def solve():
            if len(per) == len(nums):
                ans.append(per.copy())
                return 
            for i in range(len(nums)):
                if not pick[i]:
                    per.append(nums[i])
                    pick[i] = True
                    solve()
                    per.pop()
                    pick[i] = False
        solve()
        
        return ans

