class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "*+/-":
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "*":
                    c = a * b 
                elif i =="/":
                    c = int(a / b)
                elif i == "+":
                    c = a + b
                elif i == "-":
                    c = a - b
                stack.append(c)
            else:
                stack.append(i)
        return int(stack.pop())