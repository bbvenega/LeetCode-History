class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            t = temperatures[i]

            while stack and temperatures[stack[-1]] < t:
                d = stack.pop()
                ans[d] = i - d 
            
            stack.append(i)

            

        return ans 