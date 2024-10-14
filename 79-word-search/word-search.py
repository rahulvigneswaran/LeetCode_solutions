class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        # visited = set()
        wordIndex = 0
        
        def dfs(R, C, wordIndex):
            if (0
                or R < 0 or C < 0
                or R == ROWS or C == COLS
                or board[R][C] != word[wordIndex]):
                return False
            if wordIndex == len(word)-1:
                return True
            
            # visited.add((R, C))
            board[R][C] = "#"
            directions = [[1,0], [0,1], [-1, 0], [0,-1]]
            for dr, dc in directions:
                if dfs(R+dr, C+dc, wordIndex+1):
                    # visited.remove((R, C))
                    return True
            
            board[R][C] = word[wordIndex]
            # visited.remove((R, C))
            return False

        for R in range(ROWS):
            for C in range(COLS):
                if dfs(R, C, wordIndex):
                    return True
        return False