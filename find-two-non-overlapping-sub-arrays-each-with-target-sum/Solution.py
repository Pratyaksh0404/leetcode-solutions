class Solution:
    def minSumOfLengths(self, arr: List[int], tar: int) -> int:
        n = len(arr)
        INF = float('inf')
        mini = [INF] * n
        ans = INF
        left = 0
        curr = 0

        for right in range(n):
            curr += arr[right]

            while curr > tar:
                curr -= arr[left]
                left += 1

            if right > 0:
                mini[right] = mini[right - 1]

            if curr == tar:
                curr_len = right - left + 1
                if left > 0 and mini[left - 1] != INF:
                    ans = min(ans, mini[left - 1] + curr_len)
                mini[right] = min(mini[right], curr_len)

        return ans if ans != INF else -1