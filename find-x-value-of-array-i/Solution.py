class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for i in nums:
            rem = i % k
            ndp = [0] * k

            ndp[rem] += 1

            for r in range(k):
                nr = (r * rem) % k
                ndp[nr] += dp[r]

            for r in range(k):
                ans[r] += ndp[r]

            dp = ndp

        return ans