class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for R in range(len(text1)-1, -1, -1):
            for C in range(len(text2)-1, -1, -1):
                if text1[R] == text2[C]:
                    grid[R][C] = 1 + grid[R+1][C+1]
                else:
                    grid[R][C] = max(grid[R+1][C], grid[R][C+1])
        return grid[0][0]

# 2DP. Always draw a table. Start from bottom right. If the element matches, do 1+diagdown. Else take max(down, right). Return grid[0][0]
# Optimal solution >> Time : O(n^2). Space : O(n^2)