class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else: # c is "*"
                leftMin -= 1 # can be ")"
                leftMax += 1 # cam be "("
            
            if leftMax < 0:
                return False # no amount of "(" will save this. )()
            
            if leftMin < 0:
                leftMin = 0
        
        return leftMin == 0