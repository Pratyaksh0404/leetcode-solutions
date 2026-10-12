class Solution:
    def maxProductPair(self, nums: list[int], tar: int) -> list[int]:
        best, maxi, seen = [-1, -1], -float('inf'), {}
        for j, v in enumerate(nums):
            comp = tar - v
            if comp in seen:
                for i in seen[comp]:
                    if nums[i] != v:
                        prod = nums[i] * v
                        if prod > maxi:
                            maxi = prod
                            best = [i, j] if nums[i] > v else [j, i]
            seen.setdefault(v, []).append(j)
            
        return best