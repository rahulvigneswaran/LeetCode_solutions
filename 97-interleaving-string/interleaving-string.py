class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # recursion
        # def dfs(L, R):
        #     # base cases
        #     if L == len(s1) and R == len(s2):
        #         return True
            
        #     includeLeft = includeRight = 0
        #     # recursion statement
        #     if L < len(s1) and s1[L] == s3[L+R]:
        #         includeLeft = dfs(L+1, R)
        #     if R < len(s2) and s2[R] == s3[L+R]:
        #         includeRight = dfs(L, R+1)

        #     return includeLeft or includeRight
        
        # return dfs(0, 0)

        # memoization
        # memo = {}

        # def dfs(L, R):
        #     # base cases
        #     if L == len(s1) and R == len(s2):
        #         return True
            
        #     if (L, R) in memo:
        #         return memo[(L, R)]

        #     includeLeft = includeRight = 0
        #     # recursion statement
        #     if L < len(s1) and s1[L] == s3[L+R]:
        #         includeLeft = dfs(L+1, R)
        #     if not includeLeft and R < len(s2) and s2[R] == s3[L+R]:
        #         includeRight = dfs(L, R+1)

        #     memo[(L, R)] = includeLeft or includeRight

        #     return includeLeft or includeRight
        
        # return dfs(0, 0)

        # Tabulation
        # # dims
        # ROWS = len(s1) + 1
        # COLS = len(s2) + 1
        

        # # Table
        # tab = [[False]*COLS for _ in range(ROWS)]

        # # base conditions
        # tab[ROWS-1][COLS-1] = True

        # for r in range(ROWS - 1, -1, -1):
        #     for c in range(COLS - 1 , -1, -1):
        #         if r < len(s1) and s1[r] == s3[r+c]:
        #             tab[r][c] = tab[r+1][c]
                
        #         if not tab[r][c] and c < len(s2) and s2[c] == s3[r+c]:
        #             tab[r][c] = tab[r][c+1]
                
        # return tab[0][0]

        # Tabulation (Space optimized)
                # dims
        ROWS = len(s1) + 1
        COLS = len(s2) + 1
        

        # Table
        prev = [False]*COLS

        # base conditions
        prev[COLS-1] = True
        for c in range(COLS - 2, -1, -1):
            prev[c] = prev[c+1] and s2[c] == s3[len(s1) + c]

        for r in range(ROWS - 2, -1, -1):
            curr = [False]*COLS
            for c in range(COLS - 1 , -1, -1):
                if r < len(s1) and s1[r] == s3[r+c]:
                    curr[c] = prev[c]
                
                if not curr[c] and c < len(s2) and s2[c] == s3[r+c]:
                    curr[c] = curr[c+1]
                
            prev = curr
        return prev[0]