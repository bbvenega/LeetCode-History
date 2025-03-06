class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {')':'(', '}':'{',']':'['}
        stack = []

        for ch in s:
        
            if ch in mapping.values():
                stack.append(ch)
            else: 
                if not stack or stack.pop() != mapping[ch]:
                    return False 
                

        if not stack:
            return True
        else:
            return False