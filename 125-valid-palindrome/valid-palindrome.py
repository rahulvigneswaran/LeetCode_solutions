class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = clean_str(s)
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

def clean_str(s):
    return [ch.lower() for ch in s if ch.isalnum()]