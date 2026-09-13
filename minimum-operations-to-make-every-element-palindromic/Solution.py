import bisect

class Solution:
    e, o = [], []
    for l in range(1, 11):
        for p in range(10 ** ((l - 1) // 2), 10 ** ((l + 1) // 2)):
            s = str(p)
            pal = int(s + s[::-1] if l % 2 == 0 else s + s[:-1][::-1])
            (e if pal % 2 == 0 else o).append(pal)

    def minOperations(self, nums: list[int]) -> int:
        v = nums  
        
        ans = 0
        even = Solution.e
        odd = Solution.o
        
        for x in v:
            arr = even if x % 2 == 0 else odd
            i = bisect.bisect_left(arr, x)
            
            if i == 0:
                ans += (arr[0] - x) // 2
            elif i == len(arr):
                ans += (x - arr[-1]) // 2
            else:
                d1 = x - arr[i - 1]
                d2 = arr[i] - x
                ans += (d1 if d1 < d2 else d2) // 2

        return ans