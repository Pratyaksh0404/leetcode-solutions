class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            c = mid * (mid + 1) // 2
            if c == n:
                return mid
            elif c < n:
                l = mid + 1
            else:
                r = mid - 1
                
        return r