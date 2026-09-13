class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        v = nums  
        n, ans = len(v), 0
        r, stk, last, cnt = [n] * n, [], {}, [0] * n
        
        for i, x in enumerate(v):
            while stk and v[stk[-1]] > x:
                r[stk.pop()] = i
            stk.append(i)

        for i in range(n - 1, -1, -1):
            nxt = last.get(v[i], n)
            cnt[i] = 1 + (cnt[nxt] if nxt < r[i] else 0)
            last[v[i]] = i
            ans += r[i] - i - cnt[i]

        return ans