from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        ans = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            curr_max = 0
            
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue
                
                dx = x2 - x1
                dy = y2 - y1
                g = math.gcd(dx, dy)
                
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                
                slopes[(dx, dy)] += 1
                curr_max = max(curr_max, slopes[(dx, dy)])
            
            ans = max(ans, curr_max + duplicates + 1)
            
        return ans