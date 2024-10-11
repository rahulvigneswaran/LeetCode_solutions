class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for r in range(len(text1)-1, -1, -1):
            for c in range(len(text2)-1, -1, -1):
                if text1[r] == text2[c]:
                    grid[r][c] = 1 + grid[r+1][c+1]
                else:
                    grid[r][c] = max(grid[r+1][c], grid[r][c+1])
        return grid[0][0]

#This is 2DP. Always draw a table. Start from bottom right. If the element matches, do 1+diagdown. Else take max(down, right). Return grid[0][0]