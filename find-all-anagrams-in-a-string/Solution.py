class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(p)
        cc = Counter(p)
        ww = Counter()

        left = 0
        ans = []

        for right in range(len(s)):
            ww[s[right]] += 1

            if right - left + 1 > n:
                ww[s[left]] -= 1

                if ww[s[left]] == 0:
                    del ww[s[left]]

                left += 1    

            if ww == cc:
                ans.append(left)

        return ans        