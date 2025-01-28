class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0

        leftMax = height[left]
        rightMax = height[right]
        while left < right:
            # print(f"Now checking left: {left} and right: {right}")

            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
            if height[left] <= height[right]:
            #    print(f"Adding {leftMax - height[left]} to total")
               ans += leftMax - height[left]  
               left += 1
            #    leftMax = max(height[leftMax], height[left])

            else:
                # print(f"Adding {rightMax - height[right]} to total")
                ans += rightMax - height[right] 
                right -= 1
                # rightMax = max(height[rightMax], height[right])
            
            # print(f"MAX IS NOW leftMax: {leftMax} and rightMax: {rightMax}")
            

        return ans  
