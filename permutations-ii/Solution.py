from itertools import permutations 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        p = list(permutations(nums)) 
        s = set(p)  
        ans = list(s)
        
        return ans