class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = [[1, 0], [0, 1]]
        base = [[1, 1], [1, 0]]
        
        while n:
            if n & 1:
                ans = [
                    [(ans[0][0] * base[0][0] + ans[0][1] * base[1][0]) % MOD, 
                     (ans[0][0] * base[0][1] + ans[0][1] * base[1][1]) % MOD],
                    [(ans[1][0] * base[0][0] + ans[1][1] * base[1][0]) % MOD, 
                     (ans[1][0] * base[0][1] + ans[1][1] * base[1][1]) % MOD]
                ]
            base = [
                [(base[0][0] * base[0][0] + base[0][1] * base[1][0]) % MOD, 
                 (base[0][0] * base[0][1] + base[0][1] * base[1][1]) % MOD],
                [(base[1][0] * base[0][0] + base[1][1] * base[1][0]) % MOD, 
                 (base[1][0] * base[0][1] + base[1][1] * base[1][1]) % MOD]
            ]
            n >>= 1
            
        return (2 * ans[0][1]) % MOD