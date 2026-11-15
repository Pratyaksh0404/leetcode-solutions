class Solution:
    def countConsistent(self, A: list[int]) -> int:
        ans = cur = 0
        sl, sr = [], []
        for i, a in enumerate(A):
            while sl and (A[sl[-1]] & a) == a < A[sl[-1]]:
                sl.pop()
            while sr and (a & sr[-1][0]) != sr[-1][0]:
                cur -= sr.pop()[1]
            left = i - (sl[-1] if sl else -1)
            cur += left
            ans += cur
            sr.append((a, left))
            sl.append(i)
            
        return ans