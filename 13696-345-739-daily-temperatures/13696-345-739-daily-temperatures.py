class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        #Create stack and answer array length of temp
        #stack will be a monotonic decrasing stack that holds indices
        stack = []
        ans = [0] * len(temperatures)


        for i in range(len(temperatures)):
            # while the top of stack is less than the current temp
            while stack and temperatures[stack[-1]] < temperatures[i]:

                #prev = the prev high index
                prev = stack.pop()

                #prev in answer is not i - prev
                ans[prev] = i - prev
                
            stack.append(i)

        return ans

            