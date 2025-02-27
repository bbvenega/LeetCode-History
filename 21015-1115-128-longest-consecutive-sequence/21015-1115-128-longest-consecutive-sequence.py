class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        myNums = set(nums)
        ans = 0
        for val in myNums:

            if val - 1 not in myNums:
                length = 1

                while val + length in myNums:
                    length += 1

                ans = max(length, ans)
        
        return ans