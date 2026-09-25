class Solution:
    def merge(self, ii: List[List[int]]) -> List[List[int]]:
        ii.sort() 
        ans = []
        prev = ii[0]

        for i in range(1, len(ii)):
            if ii[i][0] <= prev[1]:  
                prev[1] = max(prev[1], ii[i][1]) 
            else:
                ans.append(prev)
                prev = ii[i]

        ans.append(prev)
        return ans