class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        print(nums)
        for low in range(0, len(nums)):

            if low > 0  and nums[low-1] == nums[low]:
                continue
            
            mid = low + 1
            high = len(nums) - 1


            while mid < high:
                # print(f"Checking {low},{mid},{high}")
                total = nums[low] + nums[high] + nums[mid]

                if total == 0:

                    ans.append([nums[low],nums[mid],nums[high]])

                    while mid < high and nums[mid] == nums[mid+1]:
                        mid += 1

                    while high > mid and nums[high] == nums[high - 1]:
                        high -= 1

                    mid += 1
                    high -= 1

                elif total > 0:
                    high -= 1
                
                else:
                    mid += 1

        return ans