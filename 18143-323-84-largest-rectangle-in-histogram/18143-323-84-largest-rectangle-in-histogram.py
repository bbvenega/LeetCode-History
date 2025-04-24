class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        l_b = [-1] * n

        l = []

        for i in range(n):
            
            while l and heights[l[-1]] >= heights[i]:
                l.pop()

            if l:
                l_b[i] = l[-1]
            
            l.append(i)
        
        # print(f"left_b: {l_b}")


        r_b = [n] * n
        r = []
        for i in range(n-1, -1, -1):
            
            while r and heights[r[-1]] >= heights[i]:
                r.pop()

            if r:
                r_b[i] = r[-1]
            
            r.append(i)

        # print(f"right_b: {r_b}")


        ans = 0
        for i in range(n):
            l_b[i] += 1
            r_b[i] -= 1

            ans = max(ans, (r_b[i] - l_b[i] + 1) * heights[i])
        return ans