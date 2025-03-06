class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

 

        ans = 0
        

        if len(tokens) == 1:
            return int(tokens[0])

        for val in tokens:
            # print(f"VAL: {val}")
            if val.isdigit() or val.lstrip('-').isdigit():
                # print(f"VAL IS A DIGIT")
                stack.append(int(val))
            else:
                temp_ans = ans

                if stack:
                    val1 = int(stack[-1])
                    stack.pop()
                    if stack:
                        val2 = int(stack[-1])
                        stack.pop()
                    else:
                        val2 = ans

                    # print(f"Currently trying {val1} {val} {val2}")
                    if val == '*':
                        val1 *= val2
                        ans = val1
                        stack.append(str(ans))

                    elif val == '+':
                        val1 += val2
                        ans = val1
                        stack.append(str(ans))

                    elif val == '-':
                        ans = val2 - val1
                        stack.append(str(ans))
                

                    else:
                        # # print(f"Division: {val2} {val} {val1}")
                        val1 = int(val2 / val1)
                        ans = val1
                        stack.append(str(ans))
            # print(stack)

        return ans



