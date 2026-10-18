
class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        nxt = {'R': 'B', 'B': 'W', 'W': 'R'}
        prv = {'R': 'W', 'B': 'R', 'W': 'B'}

        for root in range(n):
            if len(adj[root]) > 2:
                continue

            valid = True
            stack = [(root, -1)]

            while stack:
                u, parent = stack.pop()

                for v in adj[u]:
                    if v == parent:
                        continue

                    if colors[v] != nxt[colors[u]]:
                        valid = False
                        break

                    stack.append((v, u))

                if not valid:
                    break

            if valid:
                return root

        return -1
