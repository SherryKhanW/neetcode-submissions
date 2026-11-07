class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def operator(num1, num2, op):
            num1 = int(num1)
            num2 = int(num2)

            if op == "+":
                return num1 + num2
            
            elif op == "-":
                return num1 - num2
            
            elif op == "*":
                return num1 * num2
            else:
                return int(num1/num2)

        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                new_num = operator(stack[-2], stack[-1], i)
                stack.pop()
                stack.pop()
                stack.append(new_num)

            else:
                stack.append(i)
        
        return int(stack[0])
        