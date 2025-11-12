class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # check palindrome
        def isPali(window):
            L = 0
            R = len(window) - 1
            while L <= R:
                if window[L] != window[R]:
                    return False
                L+=1
                R-=1
            return True
        
        res = []
        subset = []
        
        #dfs
        def helper(ind):
            if ind >= len(s):
                res.append(subset.copy())
                return 
            
            for j in range(ind, len(s)):
                if isPali(s[ind:j+1]):
                    subset.append(s[ind:j+1])
                    helper(j+1)
                    subset.pop()

        helper(0)

        return res


        # aab
        # a -> a -> b
        #  |-> ab