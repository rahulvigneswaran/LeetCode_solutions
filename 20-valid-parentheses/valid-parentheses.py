class Solution:
    def isValid(self, s: str) -> bool:
        paradict = {")":"(",
                    "}":"{",
                    "]":"["}
        stack = []
        for si in s:
            if len(stack) == 0 or si in ["(", "[", "{"]:
                stack.append(si)
            elif stack[-1] == paradict[si]:
                stack.pop()
            else:
                stack.append(si)
            
        return len(stack) == 0