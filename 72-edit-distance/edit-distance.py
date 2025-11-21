class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # # recursion
        # def dfs(i1, i2):
        #     # base
        #     if i2 == len(word2):
        #         return len(word1) - i1
        #     if i1 == len(word1):
        #         return len(word2) - i2

        #     # recursion statement
        #     if word1[i1] == word2[i2]:
        #         return dfs(i1+1, i2+1) # keep

        #     return min(
        #                 dfs(i1+1, i2+1),  # replace
        #                 dfs(i1+1, i2),  # delete
        #                 dfs(i1, i2+1)   # insert
        #                 ) + 1
        
        # return dfs(0, 0)

        # memoization
        # memo = {}
        # # recursion
        # def dfs(i1, i2):
        #     # base
        #     if i2 == len(word2):
        #         return len(word1) - i1
        #     if i1 == len(word1):
        #         return len(word2) - i2

        #     if (i1, i2) in memo:
        #         return memo[(i1, i2)]

        #     # recursion statement
        #     if word1[i1] == word2[i2]:
        #         return dfs(i1+1, i2+1) # keep

        #     memo[(i1, i2)] =  min(
        #                 dfs(i1+1, i2+1),  # replace
        #                 dfs(i1+1, i2),  # delete
        #                 dfs(i1, i2+1)   # insert
        #                 ) + 1

        #     return memo[(i1, i2)]
        # return dfs(0, 0)

        # Tabulation
        #dims
        ROWS = len(word1) + 1
        COLS = len(word2) + 1

        tab = [[0]*COLS for _ in range(ROWS)]

        # base conditions
        for r in range(ROWS):
            tab[r][-1] = len(word1) - r

        for c in range(COLS):
            tab[-1][c] = len(word2) - c

        for r in range(ROWS-2, -1, -1):
            for c in range(COLS-2, -1, -1):
                if word1[r] == word2[c]:
                    tab[r][c] = tab[r+1][c+1]
                    continue
                
                tab[r][c] = min(tab[r+1][c+1], tab[r+1][c], tab[r][c+1]) + 1
        return tab[0][0]

        # # recursion
        # def dfs(i1, i2):
        #     # base
        #     if i2 == len(word2):
        #         return len(word1) - i1
        #     if i1 == len(word1):
        #         return len(word2) - i2

        #     if (i1, i2) in memo:
        #         return memo[(i1, i2)]

        #     # recursion statement
        #     if word1[i1] == word2[i2]:
        #         return dfs(i1+1, i2+1) # keep

        #     memo[(i1, i2)] =  min(
        #                 dfs(i1+1, i2+1),  # replace
        #                 dfs(i1+1, i2),  # delete
        #                 dfs(i1, i2+1)   # insert
        #                 ) + 1

        #     return memo[(i1, i2)]
        # return dfs(0, 0)
