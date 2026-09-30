class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0] * len(seq)
        f = 0
        for i, ch in enumerate(seq):
            if ch == '(':
                f += 1
                ans[i] = f % 2
            else:
                ans[i] = f % 2
                f -= 1

        return ans