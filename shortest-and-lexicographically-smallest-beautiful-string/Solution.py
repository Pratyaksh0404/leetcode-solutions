class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i] == '0': 
                continue
            ones = 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    sub = s[i:j+1]
                    if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                        ans = sub
                    break
        return ans