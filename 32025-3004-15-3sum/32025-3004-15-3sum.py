class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print("begin")
        nums.sort()
        ans = []
        i = 0
        

        while i < len(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            k = i + 1
            j = len(nums) - 1
            while k < j:
                # print(f"Current index: i: {i} k: {k} j: {j}")
                sum = nums[i] + nums[k] + nums[j]
                # print(f"sum is {sum}")
                if sum == 0:
                    ans.append([nums[i], nums[k], nums[j]])
                    while  k < j and nums[k+1] == nums[k]:
                        k += 1
                    while  j < k and nums[j-1] == nums[j]:
                        j -= 1
                    
                    k += 1
                    j -= 1

                elif sum < 0:
                    k += 1

                elif sum > 0:
                    j -= 1
                

                
            i += 1
        return ans



