import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        t = []
        for _, h in envelopes:
            idx = bisect.bisect_left(t, h)
            if idx == len(t):
                t.append(h)
            else:
                t[idx] = h

        return len(t)