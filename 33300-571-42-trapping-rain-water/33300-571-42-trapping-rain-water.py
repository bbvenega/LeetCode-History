class Solution:
    def trap(self, height: List[int]) -> int:


        left = 0
        right = len(height) - 1

        ans = 0


        left_max = height[left]
        right_max = height[right]
        while left < right:

            # print(f"Now checking {left} and {right}")
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
            
            # print(f"ans is now: {ans}\n")

        return ans 



        