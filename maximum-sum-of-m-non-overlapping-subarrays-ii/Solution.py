from collections import deque

class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]

        best_single = -float('inf')
        dq = deque()
        for i in range(l, n + 1):
            j = i - l
            while dq and P[dq[-1]] >= P[j]:
                dq.pop()
            dq.append(j)
            while dq[0] < i - r:
                dq.popleft()
            v = P[i] - P[dq[0]]
            if v > best_single:
                best_single = v

        if best_single <= 0:
            return int(best_single)

        def solve(x):
            gv = [0] * (n + 1)
            gc = [0] * (n + 1)
            kv = [0] * (n + 1)
            kc = [0] * (n + 1)
            d = deque()
            for i in range(1, n + 1):
                j = i - l
                if j >= 0:
                    vj = gv[j] - P[j]
                    cj = gc[j]
                    kv[j] = vj
                    kc[j] = cj
                    while d:
                        b = d[-1]
                        if kv[b] < vj or (kv[b] == vj and kc[b] >= cj):
                            d.pop()
                        else:
                            break
                    d.append(j)
                lim = i - r
                while d and d[0] < lim:
                    d.popleft()
                bv = gv[i - 1]
                bc = gc[i - 1]
                if d:
                    f = d[0]
                    cv = P[i] - x + kv[f]
                    cc = kc[f] + 1
                    if cv > bv or (cv == bv and cc < bc):
                        bv = cv
                        bc = cc
                gv[i] = bv
                gc[i] = bc
            return gv[n], gc[n]

        lo, hi = 0, int(best_single)
        while lo < hi:
            mid = (lo + hi) // 2
            _, c = solve(mid)
            if c <= m:
                hi = mid
            else:
                lo = mid + 1
        v, c = solve(lo)
        return int(v + lo * m)