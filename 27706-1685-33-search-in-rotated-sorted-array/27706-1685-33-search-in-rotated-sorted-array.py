class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #initiate binary search
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + ((right - left) // 2))

            # if the mid value is the target, return it
            if nums[mid] == target:
                return mid
            

            # if the left value is less than the mid value...
            if nums[left] <= nums[mid]:

                #... and the left < target < mid
                if target >= nums[left] and target <= nums[mid]:
                    right = mid -1 
                else:
                    left = mid + 1
            
            # if the left value is not less than the mid value ...
            else:

                #... and the mid < target < right
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1
        
        return -1
