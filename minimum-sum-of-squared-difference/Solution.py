class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        dif = [abs(a - b) for a, b in zip(nums1, nums2)]
        ans = k1 + k2
        
        if sum(dif) <= ans:
            return 0
            
        lo, hi = 0, max(dif)
        best = hi
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if sum(max(0, d - mid) for d in dif) <= ans:
                best = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        rem = ans - sum(max(0, d - best) for d in dif)
        return sum(min(d, best) ** 2 for d in dif) - rem * (2 * best - 1 if rem > 0 else 0)