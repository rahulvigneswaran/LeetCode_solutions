class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]

        colVisited = set()
        posDiagVisited = set() # c+r
        negDiagVisited = set() # c-r

        def helper(r):
            if r == n:
                a = ["".join(row) for row in board]
                res.append(a)
                return
            
            for c in range(n):
                if (c in colVisited 
                    or r+c in posDiagVisited
                    or r-c in negDiagVisited):
                    continue
                
                # going into recursion stack
                board[r][c] = "Q"
                colVisited.add(c)
                posDiagVisited.add(r+c)
                negDiagVisited.add(r-c)

                helper(r+1)

                # coming out of recursion stack
                board[r][c] = "."
                colVisited.remove(c)
                posDiagVisited.remove(r+c)
                negDiagVisited.remove(r-c)

        helper(0)

        return res