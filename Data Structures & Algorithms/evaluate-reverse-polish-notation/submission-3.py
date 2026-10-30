class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            total = 0
            if token == '+':
                total = stack.pop() + stack.pop()
                stack.append(total)
            elif token == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == '*':
                total = stack.pop() * stack.pop()
                stack.append(total)
            elif token == '/':
                first = stack.pop()
                second = stack.pop()
                total = second / first
                stack.append(int(total))
            else:
                token = int(token)
                stack.append(token)
        return stack.pop()