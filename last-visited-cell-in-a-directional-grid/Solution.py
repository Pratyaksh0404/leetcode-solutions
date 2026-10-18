
class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        vis = [bytearray(n) for _ in range(m)]
        vis[0][0] = 1

        moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        r = c = 0

        while True:
            dr, dc = moves[grid[r][c]]
            nr, nc = r + dr, c + dc

            if not (0 <= nr < m and 0 <= nc < n) or vis[nr][nc]:
                return [r, c]

            vis[nr][nc] = 1
            r, c = nr, nc
