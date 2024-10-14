class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        targetCount = Counter(t)
        window = {}
        have = 0 
        need = len(targetCount)
        L = 0
        res = [ ]
        resLen = float("inf")

        for R in range(len(s)):
            letter = s[R]
            window[letter] = window.get(letter, 0) + 1
            if letter in targetCount and window[letter] == targetCount[letter]:
                have+=1
                
            while have == need:
                slideLetter = s[L]
                if (R - L + 1) < resLen:
                    res = [L,R]
                    resLen = R - L + 1
                window[slideLetter]-=1
                if slideLetter in targetCount and window[slideLetter] < targetCount[slideLetter]:
                    have-=1
                L+=1
        
        return s[res[0]:res[1]+1] if resLen != float("inf") else ""

# Have, Need. If have = Need, increase L. If have < Need increase R