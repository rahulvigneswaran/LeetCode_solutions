class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [0]*n
        rows[-1] = 1
        grid = [rows]*m
        grid[-1] = [1]*n

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                grid[r][c] = grid[r+1][c] + grid[r][c+1]
        
        return grid[0][0]
                
        