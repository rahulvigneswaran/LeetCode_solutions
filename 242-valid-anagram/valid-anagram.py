class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t) or len(s) != len(t):
            return False
        s, t = list(s), list(t)
        s.sort(), t.sort()
        return s == t