class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        f = ans = 0

        for x in nums:
            if x < target:
                f += 1
            elif x == target:
                ans += 1

        return list(range(f, f + ans))