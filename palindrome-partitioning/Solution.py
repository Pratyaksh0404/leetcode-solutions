class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def palindrome(a):
            return a == a[::-1]

        def dfs(i,curr):
            if i == len(s):
                ans.append(curr)
                return 
            for j in range(i,len(s)):
                f = s[i:j+1]
                if palindrome(f):
                    dfs(j+1, curr + [f] )
            return 

        dfs(0,[])
        return ans
            