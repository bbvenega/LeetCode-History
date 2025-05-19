class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left_stack = []
        left_bounds = [-1] * n

        for i in range(n):

            while left_stack and heights[left_stack[-1]] >= heights[i]:
                left_stack.pop()
            
            if left_stack:
                left_bounds[i] = left_stack[-1]
            left_stack.append(i)

        right_stack = []
        right_bounds = [n] * n

        for i in range(n -1, -1, -1):

            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            
            if right_stack:
                right_bounds[i] = right_stack[-1]
            right_stack.append(i)

            # print(f"right_stack: {right_stack} and right_bounds: {right_bounds}\n")

        ans = 0

        for i in range(n):
            left_bounds[i] += 1
            right_bounds[i] -= 1

            ans = max(ans, (right_bounds[i] - left_bounds[i] + 1) * heights[i])
        return ans

            

