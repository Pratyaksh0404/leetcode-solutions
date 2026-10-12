from bisect import bisect_left
from heapq import merge

class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        p = {x: i for i, x in enumerate(target)}
        root = {}
        for idx, w in enumerate(words):
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = idx
        
        def dfs(node):
            children = [node[c] for c in node if c != '#']
            d = len(children)
            res = [dfs(v) for v in children]
            
            inv = sum(r[0] for r in res)
            lsts = [r[1] for r in res]
            
            c = [[0] * d for _ in range(d)]
            for i in range(d):
                for j in range(d):
                    if i == j:
                        continue
                    ai, aj = lsts[i], lsts[j]
                    q = 0
                    s = 0
                    for x in ai:
                        while q < len(aj) and aj[q] < x:
                            q += 1
                        s += q
                    c[i][j] = len(ai) * len(aj) - s
            
            dp = [10**18] * (1 << d)
            parent_mask = [-1] * (1 << d)
            last_child = [-1] * (1 << d)
            dp[0] = 0
            
            for mask in range(1 << d):
                if dp[mask] == 10**18:
                    continue
                for j in range(d):
                    if not (mask & (1 << j)):
                        add = 0
                        for i in range(d):
                            if mask & (1 << i):
                                add += c[i][j]
                        nxt = mask | (1 << j)
                        if dp[mask] + add < dp[nxt]:
                            dp[nxt] = dp[mask] + add
                            parent_mask[nxt] = mask
                            last_child[nxt] = j
            
            inv += dp[(1 << d) - 1]
            
            order = []
            curr = (1 << d) - 1
            while curr > 0:
                order.append(last_child[curr])
                curr = parent_mask[curr]
            order.reverse()
            
            opt_lsts = [lsts[j] for j in order]
            v = list(merge(*opt_lsts)) if opt_lsts else []
            
            if '#' in node:
                x = p[node['#']]
                inv += bisect_left(v, x)
                v.insert(bisect_left(v, x), x)
            
            return inv, v
        
        return dfs(root)[0]