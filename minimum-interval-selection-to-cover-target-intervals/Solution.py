class Solution:
    def minSelection(self, ai: List[List[int]], ti: List[List[int]]) -> int:
        ti.sort()
        tar = []
        for s,e in ti:
            if tar and s<=tar[-1][1]:
                tar[-1][1]=max(tar[-1][1],e)
            else:
                tar.append([s,e])
                
        ai.sort()
        ans,curr,i = 0,-1,0
        n = len(ai)
        for s,e in tar:
            if s==e:
                if curr<s:
                    mx = -1
                    while i<n and ai[i][0]<=s:
                        if ai[i][1]>=s:
                            mx = max(mx,ai[i][1])
                        i += 1
                    if mx<s:
                        return -1
                    curr = mx
                    ans += 1
            else:
                p = max(s,curr)
                while p<e:
                    mx = p
                    while i<n and ai[i][0]<=p:
                        mx = max(mx,ai[i][1])
                        i += 1
                    if mx<=p:
                        return -1
                    p = mx
                    ans += 1
                curr = max(curr,p)
        return ans
                    
                