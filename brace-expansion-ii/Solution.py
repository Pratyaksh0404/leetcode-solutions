class Solution:

    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr):
            groups = [[]]
            i = 0
            while i < len(expr):
                if expr[i] == "{":
                    depth, start = 1, i + 1
                    i += 1
                    while depth:
                        if expr[i] == "{":
                            depth += 1
                        elif expr[i] == "}":
                            depth -= 1
                        i += 1
                    groups[-1].append(parse(expr[start : i - 1]))
                elif expr[i] == ",":
                    groups.append([])
                    i += 1
                else:
                    groups[-1].append({expr[i]})
                    i += 1

            ans = set()
            for group in groups:
                cur = {""}
                for part in group:
                    cur = {x + y for x in cur for y in part}
                ans |= cur
            return ans

        return sorted(parse(expression))