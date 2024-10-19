class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visited = set()

        def dfs(R, C):
            if (R not in range(ROWS)
                or C not in range(COLS)
                or (R, C) in visited 
                or grid[R][C] == "0"):
                return
            visited.add((R, C))
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in dirs:
                dfs(R+dr, C+dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != "0" and (r,c) not in visited:
                    res+=1
                    dfs(r, c)
        
        return res

# Time complexity >> O(mn*4^(mn))