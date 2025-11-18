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
        memo = {}
        # recursion
        def dfs(i1, i2):
            # base
            if i2 == len(word2):
                return len(word1) - i1
            if i1 == len(word1):
                return len(word2) - i2

            if (i1, i2) in memo:
                return memo[(i1, i2)]

            # recursion statement
            if word1[i1] == word2[i2]:
                return dfs(i1+1, i2+1) # keep

            memo[(i1, i2)] =  min(
                        dfs(i1+1, i2+1),  # replace
                        dfs(i1+1, i2),  # delete
                        dfs(i1, i2+1)   # insert
                        ) + 1

            return memo[(i1, i2)]
        return dfs(0, 0)
