class Solution:
    def elevatorRequests(self, n: int, arr: list[int]) -> int:
        ans = 0
        curr = 0
        for i in arr:
            ans += abs(curr-i)
            curr = i

        return ans
        