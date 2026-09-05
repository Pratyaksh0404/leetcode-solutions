class Solution:
    def combinationSum2(self, cc: List[int], tar: int) -> List[List[int]]:
        cc.sort()
        ans = []
        path = []
        
        def backtrack(start, tar):
            if tar == 0:
                ans.append(path[:])  
                return
            
            for i in range(start, len(cc)):
                if i > start and cc[i] == cc[i-1]:
                    continue
                
                if cc[i] > tar:
                    break
                
                path.append(cc[i])
                
                backtrack(i + 1, tar - cc[i])
                
                path.pop()

        backtrack(0, tar)
        return ans