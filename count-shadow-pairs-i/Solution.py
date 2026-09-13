from bisect import bisect_left

class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        v = nums  
        st = []
        ans = 0
        pop = st.pop
        
        for x in v:
            ans += bisect_left(st, x)
            while st and st[-1] > x:
                pop()
            st.append(x)
            
        return ans