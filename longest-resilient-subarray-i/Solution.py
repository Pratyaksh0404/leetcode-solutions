
from math import gcd

class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1
        i = 0
        p = {}

        while i < n:
            r = nums[i] % k
            j = i + 1

            while j < n and nums[j] % k == r:
                j += 1

            length = j - i

            if r == 0:
                ans = max(ans, length)
            else:
                if r not in p:
                    p[r] = k // gcd(r, k)

                step = p[r]
                cc = 1 + ((length - 1) // step) * step
                ans = max(ans, cc)

            i = j

            if ans == n:
                return ans

        return ans
