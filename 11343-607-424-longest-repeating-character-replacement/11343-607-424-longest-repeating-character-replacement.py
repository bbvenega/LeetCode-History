class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        freq = defaultdict(int)
        maxF = 0
        ans = 0

        for right in range(len(s)):
            # print(f"Checking {left} and {right}")
            right_char = s[right]

            freq[right_char] += 1

            maxF = max(maxF, freq[right_char])

            if (right - left + 1) - maxF <= k:
                ans = max(ans, right - left + 1)
            else:
                left_char = s[left]
                freq[left_char] -= 1
                # maxF = freq[left_char]
                left += 1
            
        return ans
                



