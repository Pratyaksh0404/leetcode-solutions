class Solution:
    def grayCode(self, n: int) -> List[int]:
        nn = 1 << n 
        ans = [0]*nn
        
        for y in range(nn):
            ans[y] = y ^ (y>>1)

        return ans