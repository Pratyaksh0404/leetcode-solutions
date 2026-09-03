class Solution:
    def simplifyPath(self, p):
        ans = []
        p = p.split("/")
        for i in p:
            if ans and i == "..":
                ans.pop()
            elif i not in ["", "..", "."]:
                ans.append(i)
                
        return "/" + "/".join(ans)