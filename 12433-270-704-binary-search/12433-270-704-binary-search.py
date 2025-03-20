class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            # print(f"trying {left} and {right}")
            midpoint = left + ((right - left) // 2)
            # print(f"midpoint is {midpoint}")

            if nums[midpoint] == target:
                return midpoint
            
            if target < nums[midpoint]:
                # print(f"{target} < nums[{midpoint}]: {nums[midpoint]}\n setting right = {midpoint}")
                right = midpoint - 1
            else:
                # print(f"{target} > nums[{midpoint}]: {nums[midpoint]}\n setting left = {midpoint}")
                left = midpoint +  1
        
        return -1