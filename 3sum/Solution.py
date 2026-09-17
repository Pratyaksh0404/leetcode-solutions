class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seen = {}
        ans = set()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
      
            for j in range(i+1, n):
                left = 0 - nums[i] - nums[j]
                if left in seen and seen[left] == i:
                    ans.add(tuple(sorted([nums[i], nums[j], left])))
                seen[nums[j]] = i

        return [list(i) for i in ans]