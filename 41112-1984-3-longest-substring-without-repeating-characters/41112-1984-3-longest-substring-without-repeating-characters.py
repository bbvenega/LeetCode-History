class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0


        i = 0
        
        windowCount = set()
        windowCount.add(s[0])
        maxLen = 1

        for j in range(1, len(s)):
            # print(f"Currently checking {i} and {j}")


                # print(f"{s[j]} IS in windowCount, removing characters until it gone and updating maxLen")
            while s[j] in windowCount:

                    # print(f"Removing {s[i]} from set")
                windowCount.remove(s[i])
                i += 1
                
            windowCount.add(s[j])
            maxLen = max(maxLen, j - i + 1)
            # print(f"i: {i} j: {j} and maxLen: {maxLen}\n")
        
        return maxLen