class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dd = defaultdict(int)
        for c in t:
            dd[c] += 1

        rr = len(dd)
        l, r = 0, 0
        f = 0

        ww = defaultdict(int)
        ans = [-1, 0, 0]

        while r < len(s):
            c = s[r]
            ww[c] += 1

            if c in dd and ww[c] == dd[c]:
                f += 1

            while l <= r and f == rr:
                c = s[l]

                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r

                ww[c] -= 1
                if c in dd and ww[c] < dd[c]:
                    f -= 1

                l += 1

            r += 1

        return "" if ans[0] == -1 else s[ans[1]:ans[2]+1]
