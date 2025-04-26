class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                t1 = stack.pop()
                t2 = stack.pop()
                res = 0
                if token == '+':
                    res = t1+t2
                elif token == "-":
                    res = t2-t1
                elif token == "*":
                    res = t2*t1
                elif token == "/":
                    res = int(t2/t1)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]