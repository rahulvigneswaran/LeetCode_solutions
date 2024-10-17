class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Count = {}
        res = 0

        L = 0
        maxCount = 0
        for R in range(len(s)):
            Count[s[R]] = Count.get(s[R], 0) + 1
            maxCount = max(maxCount, Count[s[R]])

            while (R-L+1) - maxCount > k:
                Count[s[L]] -= 1
                L+=1
            
            res = max(res, R-L+1)
        
        return res