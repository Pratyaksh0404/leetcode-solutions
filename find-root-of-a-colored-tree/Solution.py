
class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        nxt = {'R': 'B', 'B': 'W', 'W': 'R'}
        indegree = [0] * n
        outdegree = [0] * n

        for u, v in edges:
            if nxt[colors[u]] == colors[v]:
                outdegree[u] += 1
                indegree[v] += 1
            elif nxt[colors[v]] == colors[u]:
                outdegree[v] += 1
                indegree[u] += 1
            else:
                return -1

        root = -1

        for i in range(n):
            if outdegree[i] > 2 or indegree[i] > 1:
                return -1

            if indegree[i] == 0:
                if root != -1:
                    return -1
                root = i

        return root
