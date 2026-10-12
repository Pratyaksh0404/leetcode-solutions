import math
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n%2!=0:
            return False
        m = n//2
        i = 5 * m * m + 4
        j = 5 * m * m - 4
        return math.isqrt(i)**2 == i or math.isqrt(j)**2 == j
        