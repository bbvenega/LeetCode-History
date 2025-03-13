class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        

        for symbol in tokens:
            ans = 0
            # print(f"Symbol: {symbol}\n Stack: {stack}")
            # print(f"symbol stripped: {symbol.strip('-')}")
            if symbol.isdigit():
                stack.append(int(symbol))
                continue
            if symbol.strip('-').isdigit():
                positive = int(symbol.strip('-'))
                stack.append(positive * -1)
                continue
            
            
            val_1 = stack.pop()
            val_2 = stack.pop()
            # print(f"wasn't a digit!: val_1: {val_1} and val_2: {val_2}")

            if symbol == "+":
                val_1 += val_2
                ans += val_1
            elif symbol == "-":
                val_2 -= val_1
                ans += val_2
            elif symbol == "*":
                val_1 *= val_2
                # print(f"val1 * val2 = {val_1}")
                ans += val_1
            elif symbol == "/":
                val_1 = int(val_2 / val_1)
                ans += val_1
            
            stack.append(ans)

        return stack[-1]

