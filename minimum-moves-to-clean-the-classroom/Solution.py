from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        id = [[-1] * n for _ in range(m)]
        k = sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr = r
                    sc = c
                elif classroom[r][c] == 'L':
                    id[r][c] = k
                    k += 1

        if k == 0:
            return 0

        total_mask = (1 << k) - 1

        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        q = deque()

        best[sr][sc][0] = energy
        q.append((sr, sc, 0, energy, 0))

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c, mask, e, moves = q.popleft()

            for dr, dc in dir:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1

                if ne < 0:
                    continue

                nmask = mask

                if classroom[nr][nc] == 'R':
                    ne = energy

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << id[nr][nc]

                if nmask == total_mask:
                    return moves + 1

                if ne <= best[nr][nc][nmask]:
                    continue

                best[nr][nc][nmask] = ne
                q.append((nr, nc, nmask, ne, moves + 1))

        return -1