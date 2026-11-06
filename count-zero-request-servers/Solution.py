class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        logs.sort(key = lambda l: l[1])
        f = {}                 
        ans = [0] * len(queries)
        i = j = 0                 

        for k in sorted(range(len(queries)), key = lambda k: queries[k]):
            q = queries[k]

            while j < len(logs) and logs[j][1] <= q: 
                s = logs[j][0]
                f[s] = f.get(s, 0) + 1
                j += 1

            while i < j and logs[i][1] < q - x:      
                s = logs[i][0]
                f[s] -= 1
                if f[s] == 0:
                    del f[s]
                i += 1

            ans[k] = n - len(f)

        return ans
