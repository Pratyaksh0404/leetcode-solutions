import math

class Solution:
    def numSquares(self, n: int) -> int:
        if math.isqrt(n)**2 == n:
            return 1
            
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
            
        for i in range(1, math.isqrt(n) + 1):
            if math.isqrt(n - i * i)**2 == n - i * i:
                return 2
                
        return 3