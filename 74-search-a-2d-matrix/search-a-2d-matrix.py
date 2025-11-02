class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do bs rowise just on the first col, then do a bn in the row
        L = 0
        R = len(matrix) - 1

        while L <= R:
            mid = L + (R-L) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        # now either we already found or we hit break cond
        row = R
        if R < 0:
            return False
                   
        L, R = 0, len(matrix[0]) - 1
        while L <= R:
            mid = L + (R-L) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        return False