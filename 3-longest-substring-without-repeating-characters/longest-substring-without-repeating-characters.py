class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        Longest = 0
        l = 0 
        r = l+1
        while l < r and r <= len(s):
            SubString = s[l:r]
            if len(SubString) == len(set(SubString)):
                Longest = max(Longest, len(SubString))
                r+=1
            else:
                l+=1
        return Longest



        