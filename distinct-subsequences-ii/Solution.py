class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        a = [0] * 26
        
        for ch in s:
            ind = ord(ch) - ord('a')
            dp1 = dp
            dp = (2 * dp - a[ind] + MOD) % MOD
            a[ind] = dp1
        
        return (dp - 1 + MOD) % MOD