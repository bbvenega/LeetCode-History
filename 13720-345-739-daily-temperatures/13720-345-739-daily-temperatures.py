class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        #initalize 0 array
        ans = [0] * n
        
        stack = []

        for i in range(n):
            
            #while the stack has values and the current index temp is greater than the previous max
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()

                # update the previous max to the distance between itself and current index
                ans[prev] = i - prev 
            
            # append the new hottest day
            stack.append(i)
        
        return ans
