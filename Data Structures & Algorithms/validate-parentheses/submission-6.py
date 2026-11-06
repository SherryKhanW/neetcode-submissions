class Solution:
    def isValid(self, s: str) -> bool:
        vals = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for i in s:
            if i in vals:
                if stack and stack[-1] == vals[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i) 
        
        return True if not stack else False