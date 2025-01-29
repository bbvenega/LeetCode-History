class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        i = 0
        maxL = 0

        chars = set()
       

        for j in range(len(s)):

            while s[j] in chars:
                chars.remove(s[i])
                i += 1

            chars.add(s[j])

            maxL = max(maxL, j - i + 1)
                
                
            
            
            # print(f"The current length is {j - i} and the max length is {maxL}\n")

        return maxL


