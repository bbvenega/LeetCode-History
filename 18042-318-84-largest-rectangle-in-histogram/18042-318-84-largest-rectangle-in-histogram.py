class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        n = len(heights)
        # initalize left most which tracks the leftmost the current bar can expand w/out
        # encountering a smaller bar
        leftMost = [-1] * n

        # 1, 2, 3... n
        for i in range(n):

            # While the height of the current left boundary is greater than the current height
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            # If there is a left boundary, set the current index to it
            if stack:
                leftMost[i] = stack[-1]
            
            stack.append(i)
        
        # Reset stack, and initailze right most which tracks the right boundary
        stack = []
        rightMost = [n] * n

        # n, n-1, n-2, ... 0
        for i in range(n - 1, -1, -1):
            # While the height of the current index in stack is greater than current height
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            # If there is a right boundary found, set the current index to stack boundary
            if stack:
                rightMost[i] = stack[-1]
            
            stack.append(i)        
        
        ans = 0

        for i in range(n):
            # Pinch in index
            leftMost[i] += 1
            rightMost[i] -= 1

            #set max answer to the height * the right boundary - left boundary
            ans = max(ans, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return ans
