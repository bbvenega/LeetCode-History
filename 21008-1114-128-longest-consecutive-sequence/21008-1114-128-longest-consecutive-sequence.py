class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myNums = set(nums)
        maxL = 0

        # length = 1

        for val in myNums:
            
            if val - 1 not in myNums:

                length = 1

                while val + length in myNums:
                    # print(f"found {val + length} in myNums")
                    length += 1


                maxL = max(maxL, length)
            
        return maxL