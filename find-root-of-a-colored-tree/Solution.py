from collections import deque
class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n,a = len(colors),[[] for _ in range(len(colors))]
        for u,v in edges:
            a[u].append(v)
            a[v].append(u)
        s = {'R':'RBW','B':'BWR','W':'WRB'}
        for i in range(n):
            q,v,ok = deque([(i,0)]),{i},True
            while q and ok:
                u,d = q.popleft()
                if colors[u]!= s[colors[i]][d%3]:
                    ok = 0
                    break
                c = 0
                for x in a[u]:
                    if x not in v:
                        v.add(x)
                        c += 1
                        q.append((x,d+1))
                if c>2:
                    ok = 0
            if ok:
                return i
        return -1