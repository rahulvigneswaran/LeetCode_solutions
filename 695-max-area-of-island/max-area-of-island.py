class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def helper(r, c, area):
            if (r, c) in visited or not(0 <= r < ROWS) or not(0 <= c < COLS) or grid[r][c] == 0:
                return 0
            
            area = 1
            visited.add((r, c))

            dirs = [[1,0], [0,1], [-1,0], [0, -1]]

            for _dir in dirs:
                area += helper(r+_dir[0], c+_dir[1], area)
            
            return area
        
        for ind_r in range(ROWS):
            for ind_c in range(COLS):
                if (ind_r, ind_c) not in visited:
                    newArea = helper(ind_r, ind_c, 0) 
                    maxArea = max(newArea, maxArea)
        return maxArea
        