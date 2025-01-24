class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i = 0
        maxL = 0
        char_set = set()

        for j in range(len(s)):
            # Move the left pointer until the current character is not a duplicate
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1

            # Add the current character to the set
            char_set.add(s[j])
            # Update the maximum length of the substring
            maxL = max(maxL, j - i + 1)

        return maxL
