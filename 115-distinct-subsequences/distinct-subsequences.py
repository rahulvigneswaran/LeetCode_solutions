class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            
            a,b = 0, 0
            if s[i] == t[j]:
                a = dfs(i+1, j+1)
            b = dfs(i+1, j)

            dp[(i, j)] = a + b
            return dp[(i, j)]

        return dfs(0, 0)