class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        for num in nums:
            w, d = num % 10, str(num // 10)
            ans = (ans + pow(int(d[:w]), int(d[w:]), MOD)) % MOD
        return ans