class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        start = 1
        if start > k:
            return -1

        INF = 10**30
        dist = {(0, start): 0}
        pq = [(0, 0, start)]

        while pq:
            d, u, run = heapq.heappop(pq)

            if d != dist.get((u, run), INF):
                continue

            if u == n - 1:
                return d

            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    nrun = run + 1
                else:
                    nrun = 1

                if nrun > k:
                    continue

                nd = d + w
                state = (v, nrun)

                if nd < dist.get(state, INF):
                    dist[state] = nd
                    heapq.heappush(pq, (nd, v, nrun))

        return -1