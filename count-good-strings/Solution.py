class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def f(k):
            if not k: 
                return 0, 1
            a, b = f(k >> 1)
            c = (a * ((b << 1) - a)) % MOD
            d = (a * a + b * b) % MOD
            return (d, (c + d) % MOD) if k & 1 else (c, d)
            
        return (f(n)[0] << 1) % MOD