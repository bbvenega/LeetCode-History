class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tCounter = Counter(t)

        formed = 0

        req = len(t)

        freq = defaultdict(int)

        left = 0

        minL = 1000000000
        minWindow = (0,0)
        

        for right in range(len(s)):
            # print(f"Left: {left} and right: {right}")

            right_char = s[right]

            if right_char in tCounter and freq[right_char] < tCounter[right_char]:
                formed += 1
                # print(f"Incrementing formed: {formed}")
            
            freq[right_char] += 1

            while left <= right and formed == req:

                left_char = s[left]
                freq[left_char] -= 1

                if right - left + 1 < minL:
                    minL = right - left + 1
                    minWindow = (left, right)

                if left_char in tCounter and freq[left_char] < tCounter[left_char]:
                    formed -= 1
            
                left += 1

        if minL == 1000000000:
            return ""
            
        return s[minWindow[0]:minWindow[1] + 1]

        