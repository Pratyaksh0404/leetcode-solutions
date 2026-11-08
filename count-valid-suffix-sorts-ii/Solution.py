class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> list[int]:
        n, m = len(nums), len(target)
        ans = [0] * (m - n + 1)
        
        com = nums + [0] + target
        z = [0] * len(com)
        L = R = 0
        for i in range(1, len(com)):
            if i <= R:
                z[i] = min(R - i + 1, z[i - L])
            while i + z[i] < len(com) and com[z[i]] == com[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > R:
                L, R = i, i + z[i] - 1
                
        pre = [0] * m
        for i in range(1, m):
            pre[i] = pre[i - 1] if target[i - 1] >= target[i] else i
            
        freq = [0] * 100001
        bad = 0
        
        def solve(f, x, delta):
            nonlocal bad
            if f[x] > 0 and f[x] + delta == 0:
                bad -= 1
            elif f[x] == 0 and f[x] + delta > 0:
                bad += 1
            f[x] += delta
            
        for x in nums:
            solve(freq, x, -1)
        for i in range(n):
            solve(freq, target[i], 1)
            
        for k in range(m - n + 1):
            if bad == 0:
                right = k + n - 1
                minI = max(0, pre[right] - k)
                maxI = min(n - 1, z[n + 1 + k])
                if maxI >= minI:
                    ans[k] = maxI - minI + 1
                    
            if k + n < m:
                solve(freq, target[k], -1)
                solve(freq, target[k + n], 1)
                
        return ans