class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        maxF = 0
        length = 0
        ans = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            # print(f"Checking indices {left} and {right}")
            ch = s[right]

            freq[ch] += 1

            maxF = max(maxF, freq[ch])

            if (right - left + 1) - maxF <= k:
                ans = max(ans, right - left + 1)
            else:
                freq[s[left]] -= 1
                left += 1
        
        # ans = max(ans, right - left + 1)
        return ans
