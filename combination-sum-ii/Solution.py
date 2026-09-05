class Solution:
    def combinationSum2(self, cc: List[int], tar: int) -> List[List[int]]:
        cc.sort() 
        ans = []

        def solve(start, tar, path):
            if tar == 0:
                ans.append(path)
                return
            
            for i in range(start, len(cc)):
                if i > start and cc[i] == cc[i-1]:
                    continue
                
                if cc[i] > tar:
                    break
                
                solve(i + 1, tar - cc[i], path + [cc[i]])

        solve(0, tar, [])
        return ans