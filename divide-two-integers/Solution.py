class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b, q = abs(dividend), abs(divisor), 0
        
        for i in reversed(range(32)):
            if a >= (x := b << i):
                a -= x
                q += 1 << i
                
        q = q if (dividend < 0) == (divisor < 0) else -q
        return min(max(-2**31, q), 2**31 - 1)