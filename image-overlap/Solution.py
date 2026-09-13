class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        aa, bb, d = [], [], collections.defaultdict(int)

        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]:
                    aa.append((r, c))

                if B[r][c]:
                    bb.append((r, c))
 
        for ra, ca in aa:
            for rb, cb in bb:
                d[(rb - ra, cb - ca)] += 1

        return max(d.values() or [0])