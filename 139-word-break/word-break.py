class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # naive recursive
        # def helper(i):
        #     if i == len(s):
        #         return True
            
        #     for word in wordDict:
        #         if s[i:i+len(word)] == word:
        #             return helper(i+len(word))
            
        #     return False
        # return helper(0)

        # memo
        # memo = {}
        # def helper(i):
        #     if i == len(s):
        #         return True
            
        #     if i in memo:
        #         return memo[i]
        #     for word in wordDict:
        #         if s[i:i+len(word)] == word:
        #             memo[i] = helper(i+len(word))
        #             return memo[i]
        #     memo[i] = False
        #     return memo[i]
        # return helper(0)

        # tab
        tab = [False]*(len(s)+1)
        tab[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    tab[i] = tab[i+len(word)]
                    if tab[i]: break
        
        return tab[0]

        