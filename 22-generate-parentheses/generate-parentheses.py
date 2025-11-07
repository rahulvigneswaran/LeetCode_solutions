class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def helper(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                helper(openN+1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                helper(openN, closeN+1)
                stack.pop()
        
        helper(0, 0)
        return res