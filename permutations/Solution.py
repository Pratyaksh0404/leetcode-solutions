class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        pick = [False]*len(nums)
        
        def solve():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return 
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    solve()
                    perm.pop()
                    pick[i] = False
        solve()
        
        return ans

