class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}

        stack = []

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:

                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False