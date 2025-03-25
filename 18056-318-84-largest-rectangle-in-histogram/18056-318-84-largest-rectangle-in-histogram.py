class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_b = []
        left = [-1] * n
        right = [n] * n        

        right_b = []


        for i in range(n):

            while left_b and heights[left_b[-1]] >= heights[i]:
                left_b.pop()

            if left_b:
                left[i] = left_b[-1]

            left_b.append(i)
            # print(f"left_B: {left_b}\nleft: {left}")

        for i in range(n-1, -1, -1):
            # print(f"r{i}")
            while right_b and heights[right_b[-1]] >= heights[i]:
                right_b.pop()

            if right_b:
                right[i] = right_b[-1]
            right_b.append(i)
        
        ans = float("-inf")

        for i in range(n):
            left[i] += 1
            right[i] -= 1

            ans = max(ans, heights[i] * (right[i] - left[i] + 1))
            
        return ans 