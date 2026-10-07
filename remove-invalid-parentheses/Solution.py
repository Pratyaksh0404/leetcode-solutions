
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        ans = []
        self.visited = set()
        self.dfs(s, self.invalid(s), ans)
        return ans
    
    def dfs(self, s, n, ans):
        if n == 0:
            
            ans.append(s)
            return
        
        
        for i in range(len(s)):
            
            if s[i] in ('(',')'):
        
                new_s = s[:i]+s[i+1:]
                vsr=self.invalid(new_s)
                
                if new_s not in self.visited and vsr < n:
                    self.visited.add(new_s)
                    
                    
                    self.dfs(new_s, vsr, ans)
        
    def invalid(self, s):
      st=[]
      for i,v in enumerate (s):
        if chr(97)<= v <=chr(122) : continue
          
        if v=="(":
          st.append(v)
          
        elif len(st)==0 or st[-1]!="(":
          st.append(v)
          
        elif v==")" and st[-1]=="(": 
          st.pop()
          
        
      return len(st)
          
          