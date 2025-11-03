class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        
        # dfs to note down all 0-s that cannot be surrounded
        def helper(r, c):
            if (not(0 <= r < ROWS) or not(0 <= c < COLS)
                or board[r][c] != "O"):
                return 
            
            board[r][c] = "Z"
            helper(r+1, c)
            helper(r-1, c)
            helper(r, c+1)
            helper(r, c-1)
        
        for r in range(ROWS):
            if board[r][0] == "O":
                helper(r, 0)
            if board[r][-1] == "O":
                helper(r, COLS-1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                helper(0, c)
            if board[-1][c] == "O":
                helper(ROWS-1, c)

        # traverse through all to make surrounded as "X" and revert non sourroudn back
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Z":
                    board[r][c] = "O"