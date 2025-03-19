class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            # print(f"{i}: Stack:{stack} and ans: {ans}")
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()

                ans[prev] = i - prev
            stack.append(i)
        
        # print(f"FINAL: Stack:{stack} and ans: {ans}")

        return ans