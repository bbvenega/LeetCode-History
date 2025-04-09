class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        ans = nums[0]
        

        while left <= right:

            mid = left + ((right - left ) // 2)
            # print(f"l: {left} r: {right} and m: {mid}")

            if nums[mid] >= nums[0]:
                left = mid + 1

            else:
                ans = nums[mid]
                right = mid - 1
        
        return ans

