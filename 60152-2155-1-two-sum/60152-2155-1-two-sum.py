class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comp = {}

        for i in range(len(nums)):
            # print(f"Comp is currently {comp}\n")
            remain = target - nums[i]

            if target - remain in comp:
                return [i, comp[target - remain]]
            
            comp[remain] = i
        
        return [0,0]
