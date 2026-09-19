class Solution:
    def score(self, cards: List[str], x: str) -> int:
        both = 0
        cnt1, cnt2 = collections.defaultdict(int), collections.defaultdict(int)
        for c in cards:
            if c == x + x:
                both += 1
            elif c[0] == x:
                cnt1[c[1]] += 1
            elif c[1] == x:
                cnt2[c[0]] += 1
        
        v1 = sorted(cnt1.values(), reverse=True)
        v2 = sorted(cnt2.values(), reverse=True)
        
        def solve(cnt, have):
            s = sum(cnt) + have
            m = max(cnt[0] if cnt else 0, have)
            return min(s // 2, s - m)
        
        return max(solve(v1, i) + solve(v2, both - i) for i in range(both + 1))