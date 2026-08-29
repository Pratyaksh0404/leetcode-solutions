class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((num, i) for i, num in enumerate(nums))
        ans = [0] * len(nums)
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and arr[j][0] - arr[j-1][0] <= limit:
                j += 1
            for idx, (val, _) in zip(sorted(arr[k][1] for k in range(i, j)), arr[i:j]):
                ans[idx] = val
            i = j
        return ans