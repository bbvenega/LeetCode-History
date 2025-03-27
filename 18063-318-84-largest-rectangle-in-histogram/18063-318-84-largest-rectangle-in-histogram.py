class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left = [-1] * n

        stack = []
        for i in range(n):

            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                left[i] = stack[-1]
            stack.append(i)


        stack = []
        right = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                right[i] = stack[-1]
            stack.append(i)

        
        ans = float("-inf")

        for i in range(n):
            right[i] -= 1
            left[i] += 1

            area = (right[i] - left[i] + 1) * heights[i]
            ans = max(ans, area)
        return ans