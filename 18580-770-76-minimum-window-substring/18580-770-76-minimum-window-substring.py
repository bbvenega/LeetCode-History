class Solution:
    def minWindow(self, s: str, t: str) -> str:
        


        minWindow = (0,0)
        minL = float("inf")

        tCounter = Counter(t)

        freq = defaultdict(int)

        formed = 0
        
        left = 0

        right = 0

        req = len(t)

        # print(f"rq: {req}")

        while right < len(s):
            # print(f"left: {left} right: {right}")
            right_char = s[right]

            freq[right_char] += 1

            # print(f"Is right_char in tCounter? {right_char in tCounter}\n freq[right_char] = {freq[right_char]} and tCounter[right_char] = {freq[right_char]}")
            if right_char in tCounter and freq[right_char] <= tCounter[right_char]:
                formed += 1
                # print(f"incrementing formed: {formed}")

            
            while left <= right and formed == req:
                
                left_char = s[left]

                freq[left_char] -= 1

                if right - left + 1 < minL:
                    # print(f"Updating minWin: {left}, {right}")
                    minL = right - left + 1
                    minWindow = (left, right)

                if freq[left_char] < tCounter[left_char]:
                    formed -= 1

                left += 1

            right += 1
        
        if minL == float("inf"):
            return ""

        return s[minWindow[0]:minWindow[1] + 1]

