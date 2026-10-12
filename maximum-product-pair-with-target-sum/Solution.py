class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        ans = [-1, -1]
        maxi = -float('inf')
        n = len(nums)
        
        for i in range(n):
            ni = nums[i]
            for j in range(i + 1, n):
                nj = nums[j]
                if ni + nj == target:
                    if ni > nj:
                        prod = ni * nj
                        if prod > maxi:
                            maxi = prod
                            ans = [i, j]
                    elif nj > ni:
                        prod = ni * nj
                        if prod > maxi:
                            maxi = prod
                            ans = [j, i]
                            
        return ans