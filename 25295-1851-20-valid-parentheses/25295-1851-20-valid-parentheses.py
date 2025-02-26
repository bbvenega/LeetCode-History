class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []


        for ch in s:

            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
                continue
            if not stack:
                return False
            top = stack[-1]
            # print(top)

            if (ch == ')' and top == '(') or (ch == ']' and top == '[') or (ch == '}' and top == '{'):
                stack.pop()
                continue
            
            # print(stack)
            return False

        if not stack:
            return True
        return False
