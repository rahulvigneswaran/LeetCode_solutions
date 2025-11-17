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
        memo = {}

        def dfs(L, R):
            # base cases
            if L == len(s1) and R == len(s2):
                return True
            
            if (L, R) in memo:
                return memo[(L, R)]

            includeLeft = includeRight = 0
            # recursion statement
            if L < len(s1) and s1[L] == s3[L+R]:
                includeLeft = dfs(L+1, R)
            if not includeLeft and R < len(s2) and s2[R] == s3[L+R]:
                includeRight = dfs(L, R+1)

            memo[(L, R)] = includeLeft or includeRight

            return includeLeft or includeRight
        
        return dfs(0, 0)