class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_stack = []
        left_b = [-1] * n

        for i in range(n):
            # print(f"{i}: left_stack: {left_stack} & left_b {left_b}")

            h = heights[i]
            while left_stack and h <= heights[left_stack[-1]]:
                left_stack.pop()
            
            if left_stack:
                left_b[i] = left_stack[-1]
            
            left_stack.append(i)
        
        # print(f"left_b: {left_b}")

        r_stack = []
        r_b = [n] * n

        for i in range(n-1, -1, -1):
            # print(f"{i}: right_stack: {r_stack} & r_b {r_b}")

            h = heights[i]
            while r_stack and h <= heights[r_stack[-1]]:
                r_stack.pop()
            
            if r_stack:
                r_b[i] = r_stack[-1]
            
            r_stack.append(i)

        # print(f"r_b: {r_b}")

        ans = float("-inf")

        for i in range(n):

            left_b[i] += 1
            r_b[i] -= 1

            ans = max(ans, ((r_b[i] - left_b[i] + 1) * heights[i]))

        return ans


