class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Longest = 0
        l = 0
        Count = {}
        for r in range(len(s)):
            Count[s[r]] = Count.get(s[r], 0) + 1

            while (r-l+1) - max(Count.values()) > k:
                Count[s[l]] -= 1
                l+=1

            Longest = max(Longest, r-l+1)
        return Longest        