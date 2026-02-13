class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(prevVal, r, c):
            if (not(0 <= r < ROWS) or
                not(0 <= c < COLS) or
                matrix[r][c] <= prevVal):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            LIP = 1 + max(dfs(matrix[r][c], r+1, c),
                        dfs(matrix[r][c], r, c+1),
                        dfs(matrix[r][c], r-1, c),
                        dfs(matrix[r][c], r, c-1),)
            
            dp[(r, c)] = LIP
            
            return LIP
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(-1, r, c)
            
        return max(list(dp.values()))