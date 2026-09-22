class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        ans = []
        maxi, p = 0, -1

        for i, c in enumerate(s):
            maxi = max(maxi, last[c])
            if i == maxi:
                ans.append(i - p)
                p = i

        return ans