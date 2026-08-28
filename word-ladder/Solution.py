class Solution:
    def ladderLength(self, b: str, e: str, wordList: List[str]) -> int:
        w = set(wordList)
        if e not in w:
            return 0
        q = deque()
        q.append(b)
        d = 1
        while q:
            l = len(q)
            for _ in range(l):
                curr = q.popleft()
                if curr == e:
                    return d
                for i in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr[i]:
                            continue  
                        new = curr[:i] + c + curr[i+1:]
                        if new in w:
                            q.append(new)
                            w.remove(new)  
            d += 1

        return 0