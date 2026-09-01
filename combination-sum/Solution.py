class Solution:
    def combinationSum(self, cc: List[int], tar: int) -> List[List[int]]:
        self.ans = []  

        def solve(c, arr,sm):                 
            if sm == tar: 
                self.ans.append(arr)      
            if sm >= tar: 
                return                     
            for i in range(len(c)):                
                solve(c[i:], arr + [c[i]], sm+c[i])   
                
        solve(cc,[], 0)
        return self.ans