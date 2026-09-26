class Solution:
    def evaluate(self, s: str, k: list[list[str]]) -> str:
        data = dict(k)

        p = s.split("(")
        ans = ""

        for i in p:
            if ")" in i:
                key, rest = i.split(")", 1)
                ans += str(data.get(key, "?")) + rest
            else:
                ans += i

        return ans