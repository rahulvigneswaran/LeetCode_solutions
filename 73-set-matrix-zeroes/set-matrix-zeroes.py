class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for R in range(ROWS):
            for C in range(COLS):
                if matrix[R][C] == 0:
                    matrix[0][C] = 0
                    if R == 0:
                        firstRowZero = True
                    else:
                        matrix[R][0] = 0 
                    
                        
        for C in range(1, COLS):
            for R in range(1, ROWS):
                if matrix[0][C] == 0 or matrix[R][0] == 0:
                    matrix[R][C] = 0

        if matrix[0][0] == 0:
            for R in range(ROWS):
                matrix[R][0] = 0
        
        if firstRowZero:
            for C in range(COLS):
                matrix[0][C] = 0
                
# Time >> O(n^2)
# Space >> O(1)