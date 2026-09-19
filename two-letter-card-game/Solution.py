class Solution:
    def score(self, cards: List[str], x: str) -> int:
        both = 0
        cnt1, cnt2 = collections.defaultdict(int), collections.defaultdict(int)
        
        for c in cards:
            if c[0] == x and c[1] == x:
                both += 1
            elif c[0] == x:
                cnt1[c[1]] += 1
            elif c[1] == x:
                cnt2[c[0]] += 1
        
        def solve(cnt):
            vals = list(cnt.values())
            s = sum(vals)
            ma = max(vals) if vals else 0
            return 0 if s < 2 else min(s // 2, s - ma)
            
        lr = sum(cnt1.values()) + sum(cnt2.values())
        if both >= lr:
            return lr
            
        return min(solve(cnt1) + solve(cnt2), (lr - both) // 2) + both