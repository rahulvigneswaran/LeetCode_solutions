class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # naive recursion
        # def helper(R, C):
        #     if R == m-1 and C == n-1:
        #         return 1
            
        #     a = b = 0

        #     if R + 1 < m:
        #         a = helper(R+1, C)
        #     if C + 1 < n:
        #         b = helper(R, C+1)
            
        #     return a + b
        # return helper(0, 0)

        # memo
        # memo = {}
        # def helper(R, C):
        #     if R == m-1 and C == n-1:
        #         return 1
            
        #     if (R, C) in memo:
        #         return memo[(R, C)]
        #     a = b = 0

        #     if R + 1 < m:
        #         a = helper(R+1, C)
        #     if C + 1 < n:
        #         b = helper(R, C+1)
            
        #     memo[(R, C)] = a + b
        #     return memo[(R, C)]
        # return helper(0, 0)
    
        # tab
        # tab = [[0]*(n+1) for _ in range(m+1)]

        # for R in range(m-1, -1, -1):
        #     for C in range(n-1, -1, -1):
        #         if R == m-1 and C == n-1:
        #             tab[R][C] = 1
        #         else:
        #             tab[R][C] = tab[R+1][C] + tab[R][C+1]
        
        # return tab[0][0]

        # tab (space optimized)
        prevtab = [1]*(n+1)

        for _ in range(m-2, -1, -1):
            currtab = [0]*(n+1)
            for C in range(n-1, -1, -1):
                currtab[C] = prevtab[C] + currtab[C+1]
            prevtab = currtab
        
        return prevtab[0]
        

        