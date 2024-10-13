class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], len(s)+1
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in countT:
                window[c] = 1 + window.get(c, 0)
                if window[c] == countT[c]:
                    have += 1

                while have == need:
                    # update our result
                    if (r - l + 1) < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    
                    newC = s[l]
                    
                    if newC in countT :
                        window[newC] -= 1
                        if window[newC] < countT[newC]:
                            have -= 1
                    l += 1
        l, r = res
        return s[l : r + 1] if resLen != len(s)+1 else ""