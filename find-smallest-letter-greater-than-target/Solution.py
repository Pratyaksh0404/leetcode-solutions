class Solution:
    def nextGreatestLetter(self, a: List[str], tar: str) -> str:
        ans = a[0]
        f = False

        for i in a:
            if not f:
                if i > tar:
                    ans = i
                    f = not f
            else:
                if i > tar and i < ans:
                    ans = i

        return ans