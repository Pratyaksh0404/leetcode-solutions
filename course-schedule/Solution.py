class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        ii = [0] * n
        ans = []

        for pair in p:
            c = pair[0]
            pp = pair[1]
            adj[pp].append(c)
            ii[c] += 1

        q = deque()
        for i in range(n):
            if ii[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            ans.append(curr)

            for i in adj[curr]:
                ii[i] -= 1
                if ii[i] == 0:
                    q.append(i)

        return len(ans) == n