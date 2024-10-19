class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        LEFT, RIGHT = 0, len(matrix[0])
        TOP, BOTTOM = 0, len(matrix)

        res = []

        while LEFT < RIGHT and TOP < BOTTOM:
            # Going LEFT -> RIGHT
            for i in range(LEFT, RIGHT):
                res.append(matrix[TOP][i])
            TOP += 1

            # Going TOP -> BOTTOM
            for i in range(TOP, BOTTOM):
                res.append(matrix[i][RIGHT - 1]) # we subtract by 1 because itll be Out of Bounds. This will be okay in range because it will be excluded.
            RIGHT -=1

            if not(LEFT < RIGHT and TOP < BOTTOM): # once we complete two adjacent edges, in case of row or column, matrix, we have covered everything
                break
            
            # Going RIGHT -> LEFT
            for i in range(RIGHT-1, LEFT-1, -1):
                res.append(matrix[BOTTOM-1][i]) # we subtract by 1 because itll be Out of Bounds. This will be okay in range because it will be excluded.
            BOTTOM -= 1

            # Going BOTTOM -> TOP
            for i in range(BOTTOM-1, TOP-1, -1):
                res.append(matrix[i][LEFT])
            LEFT += 1
        return res

# Draw and visualize. Have LEFT, RIGHT and TOP, BOTTOM counters. Once a line is done, shrink the corresponding counters in. Break if LEFT crosses RIGHT or TOP crosses BOTTOM. Have 4 loops, one for each side. Check for break after the first two, to account for column or row vectors.

# Time complexity >> O(mn)
# Space complexity >> O(1)