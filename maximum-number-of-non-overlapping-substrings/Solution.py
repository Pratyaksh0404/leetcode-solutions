class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        left = [n] * 26
        right = [0] * 26
        
        for i in range(n):
            index = ord(s[i]) - ord('a')
            left[index] = min(left[index], i)
            right[index] = i
            
        ans = []
        r = -1
        
        for i in range(n):
            if i != left[ord(s[i]) - ord('a')]:
                continue
            
            nr = right[ord(s[i]) - ord('a')]
            j = i + 1
            while j < nr + 1:
                if left[ord(s[j]) - ord('a')] < i:
                    nr = n
                    break
                nr = max(nr, right[ord(s[j]) - ord('a')])
                j += 1
                
            if nr < n:
                if i > r:
                    ans.append(s[i:nr + 1])
                else:
                    ans[-1] = s[i:nr + 1]
                r = nr
                
        return ans