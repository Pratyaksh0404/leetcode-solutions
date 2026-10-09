from collections import deque

class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]

        best = -float('inf')
        dq = deque()
        for i in range(l, n + 1):
            j = i - l
            pj = P[j]
            while dq and P[dq[-1]] >= pj:
                dq.pop()
            dq.append(j)
            while dq[0] < i - r:
                dq.popleft()
            v = P[i] - P[dq[0]]
            if v > best:
                best = v

        if best <= 0:
            return int(best)

        SH = 17
        K = 1 << SH
        PK = [p << SH for p in P]

        def solve(x):
            pen = (x << SH) + 1
            g = [0] * (n + 1)
            qi = [0] * (n + 1)
            qk = [0] * (n + 1)
            head = 0
            tail = 0
            for i in range(l, n + 1):
                j = i - l
                kj = g[j] - PK[j]
                while tail > head and qk[tail - 1] <= kj:
                    tail -= 1
                qi[tail] = j
                qk[tail] = kj
                tail += 1
                lim = i - r
                while qi[head] < lim:
                    head += 1
                cand = PK[i] - pen + qk[head]
                prev = g[i - 1]
                g[i] = cand if cand > prev else prev
            s = g[n]
            v = (s + K - 1) >> SH
            c = (v << SH) - s
            return v, c

        lo, hi = 0, int(best)
        av, ax = 0, hi
        while lo < hi:
            mid = (lo + hi) >> 1
            v, c = solve(mid)
            if c == m:
                return int(v + mid * m)
            if c < m:
                hi = mid
                av, ax = v, mid
            else:
                lo = mid + 1
        return int(av + ax * m)