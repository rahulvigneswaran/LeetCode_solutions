class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Count = {}
        Longest = 0
        
        l = 0
        MaxF = 0
        for r in range(len(s)):
            Count[s[r]] = Count.get(s[r], 0) + 1
            MaxF = max(MaxF, Count[s[r]])

            while (r-l+1) - MaxF > k:
                Count[s[l]] -= 1
                l+=1

            Longest = max(Longest, r-l+1)
        return Longest        