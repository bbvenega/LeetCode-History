class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 

        while left <= right:

            mid = left + ((right - left) // 2)
            print(f"l: {left} r: {right} mid: {mid}")
            if nums[mid] == target:
                return mid


            # if left <= nums
            if nums[left] <= nums[mid]:
                # ... and left < target < mid
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                else: 
                    left = mid + 1
            
            # if left > nums
            else:
                #... and mid <= target <= right
                if target <= nums[right] and target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 