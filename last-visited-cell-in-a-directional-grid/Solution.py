class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m,n = len(grid),len(grid[0])
        r,c,v = 0,0,{(0,0)}
        d = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
        while True:
            dr,dc = d[grid[r][c]]
            nr,nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<n and (nr,nc) not in v:
                v.add((nr,nc))
                r,c = nr,nc
            else:
                break
        return [r,c]
                   
