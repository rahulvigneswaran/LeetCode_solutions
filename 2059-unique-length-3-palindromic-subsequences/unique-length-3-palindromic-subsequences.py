class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # # naive

        # res = set()
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         for k in range(j+1, len(s)):
        #             if s[i] == s[k]:
        #                 res.add(s[i]+s[j]+s[k])
        # return len(res)
        
        # recursion (not true)
        # res = []
        # def dfs(n, window): 
        #     if len(window) == 3 and window[0] == window[-1]:
        #         res.append("".join(window))
        #         return 
        #     if n == len(s):
        #         return
            
        #     #include
        #     window.append(s[n])
        #     dfs(n+1, window)
        #     window.pop()

        #     #skip
        #     dfs(n+1, window)


        # dfs(0, [])
        # return len(set(res))
        
        # bread and filling
        letters = set(s)
        res = 0
        for letter in letters:
            # first occurence from left
            L = s.find(letter)
            R = s.rfind(letter)
            
            res+= len(set(s[L+1:R]))

        return res