class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        curr = 1000
        c = 1
        while n >= curr:
            next = curr*1000
            num = min(n,next - 1) - curr + 1
            ans += num*c
            curr = next
            c += 1

        return ans