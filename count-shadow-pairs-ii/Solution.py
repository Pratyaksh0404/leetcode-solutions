from bisect import bisect_right

class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        t = nums
        D = {x: i for i, x in enumerate(sorted(set(t)))}
        q = [([D[x] for x in t], 0, len(D))]
        ans = 0

        while q:
            B, l, r = q.pop()
            if r - l <= 1 or len(B) < 2:
                continue
            m = (l + r) // 2
            lo, hi = [], []
            for i, x in enumerate(B):
                if x < m:
                    while lo and B[lo[-1]] < x:
                        lo.pop()
                    lo.append(i)
                else:
                    while hi and B[hi[-1]] >= x:
                        hi.pop()
                    p = hi[-1] if hi else -1
                    ans += len(lo) - bisect_right(lo, p)
                    hi.append(i)
            q.append(([x for x in B if x < m], l, m))
            q.append(([x for x in B if x >= m], m, r))

        return ans