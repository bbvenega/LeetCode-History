class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []


        for ch in tokens:
            # print(f"stack: {stack}")
            if ch.isdigit():
                stack.append(int(ch))
                continue

            if ch.strip('-').isdigit():
                val = -1
                val *= int(ch.strip('-'))
                stack.append(val)
                continue
            
            val1 = stack.pop()
            val2 = stack.pop()

            if ch == '+':
                val1 += val2
                stack.append(val1)
            elif ch == '*':
                val1 *= val2
                stack.append(val1)
            elif ch == '-':
                val2 -= val1
                stack.append(val2)
            else:
                # print(f"val1 = {val1} / {val2}")
                val1 = int(val2 / val1)
                stack.append(val1)
            
        if stack:
            return stack[-1]
        else:
            return -1