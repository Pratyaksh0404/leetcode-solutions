class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9+7
        q = 0
        ans = 0

        for i in arr:
            q += i
            ans += q%2

        ans += (len(arr) - ans) * ans

        return  ans % MOD