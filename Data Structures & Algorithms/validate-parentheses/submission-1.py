

class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []



        for char in s:
            if char == '(' or char == '[' or char == '{':
                open_stack.append(char)
            if char == ']' and (len(open_stack) < 1 or open_stack.pop() != '['):
                return False
            if char == '}' and (len(open_stack) < 1 or open_stack.pop() != '{'):
                return False
            if char == ')' and (len(open_stack) < 1 or open_stack.pop() != '('):
                return False
        
        if len(open_stack) > 0:
            return False

        return True