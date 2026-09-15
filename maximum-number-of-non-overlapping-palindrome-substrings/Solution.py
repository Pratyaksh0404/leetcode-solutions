class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        def check(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(k, n + 1):
            dp[i] = dp[i - 1]
            
            if check(i - k, i - 1):
                dp[i] = max(dp[i], 1 + dp[i - k])
                
            if i > k and check(i - k - 1, i - 1):
                dp[i] = max(dp[i], 1 + dp[i - k - 1])
                
        return dp[n]