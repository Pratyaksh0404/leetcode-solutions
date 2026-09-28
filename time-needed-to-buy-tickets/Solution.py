class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        n = len(t)
        x = t[k]
        ans = 0
        for i, y in enumerate(t):
            buy = x
            if i > k: 
                buy = x-1
            ans += min(buy, y)
        return ans
        