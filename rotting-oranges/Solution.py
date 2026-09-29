class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        q = deque() 
        for idx in range(M):
            for jdx in range(N):
                if grid[idx][jdx] == 2:
                    q.append((idx, jdx, 0))
        
        ans = 0
        while q:
            idx, jdx, time = q.popleft()
            for adjX, adjY in [(idx-1, jdx), (idx+1, jdx), (idx, jdx-1), (idx, jdx+1)]:
                if adjX < 0 or adjX >= M or adjY < 0 or adjY >= N:
                    continue
                if grid[adjX][adjY] == 0 or grid[adjX][adjY] == 2:
                    continue
                
                grid[adjX][adjY] = 2
                q.append((adjX, adjY, time+1))
                ans = max(ans, time+1)
        
        for idx in range(M):
            for jdx in range(N):
                if grid[idx][jdx] == 1:
                    return -1

        return ans            