from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            l = [x for x in arr[1:] if x < root]
            r = [x for x in arr[1:] if x > root]

            wl = dfs(l)
            wr = dfs(r)

            ii = comb[len(l) + len(r)][len(l)]

            return (ii * wl * wr) % MOD

        return (dfs(nums) - 1 + MOD) % MOD