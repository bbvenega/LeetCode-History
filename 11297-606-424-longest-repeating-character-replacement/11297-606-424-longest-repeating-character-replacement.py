class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0


        left = 0
        maxF = 0
        ans = 0

        
        freq = {}

        for right in range(len(s)):
            
            leftCh = s[left]
            rightCh = s[right]

            freq[rightCh] = freq.get(rightCh, 0) + 1

            maxF = max(maxF, freq[rightCh])

            if (right - left + 1) - maxF > k:
                freq[leftCh] = freq.get(leftCh, 0) - 1
                left += 1
            else:
                ans = max(right - left + 1, ans)
        
        return ans
        