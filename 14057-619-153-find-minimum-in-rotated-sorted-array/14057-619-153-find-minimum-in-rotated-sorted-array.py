class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #initiate binary search and set answer to first index
        left = 0
        right = len(nums) - 1

        ans = nums[0]


        while left <= right:
            mid = (left + (right - left) // 2)

            # if the middle index is greater than the first value in the list
            # set left = to the middle index, as 
            if nums[mid] >= nums[0]:
                left = mid + 1

            # if the middle index is less than the first value in the list
            # set answer to the right index and bring in right value
            else:
                ans = nums[mid]
                right = mid - 1
        
        return ans
