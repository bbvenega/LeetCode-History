class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myNums = set(nums)

        maxL = 0
        for num in myNums:

            if num - 1 not in myNums:

                length = 1

                while num + length in myNums:
                    length += 1

                maxL = max(maxL, length)
        
        return maxL