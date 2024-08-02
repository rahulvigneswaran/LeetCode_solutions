class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {")": "(",
                "]": "[",
                "}": "{"}
        
        stack = []

        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == bmap.get(i):
                stack.pop()
            else:
                stack.append(i)
        
        return not(len(stack))
