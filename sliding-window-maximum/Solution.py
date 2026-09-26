class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        n = len(nums)

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        ans.append(nums[q[0]])

        for i in range(k, n):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])

        return ans