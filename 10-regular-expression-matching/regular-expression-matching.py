class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # naive
        # def dfs(i, j):
        #     if i >= len(s) and j >= len(p):
        #         return True
            
        #     if j >= len(p):
        #         return False
            
        #     match = i < len(s) and (s[i] == p[j] or p[j] == ".")

        #     if (j + 1 < len(p) and (p[j+1] == "*")):
        #         return (dfs(i, j+2) or # not use *
        #                 (match and dfs(i+1, j))) # use *

        #     if match:
        #         return dfs(i+1, j+1)
            
        #     return False
        
        # return dfs(0, 0)

        # memo
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1 < len(p) and (p[j+1] == "*")):
                memo[(i, j)] = (dfs(i, j+2) or # not use *
                                (match and dfs(i+1, j))) # use *
                return memo[(i, j)]

            if match:
                memo[(i, j)] =  dfs(i+1, j+1)
                return memo[(i, j)]
            
            return False
        
        return dfs(0, 0)

