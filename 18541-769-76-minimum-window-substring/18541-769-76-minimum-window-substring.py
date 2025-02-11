class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left = 0
        right = 0

        freq = defaultdict(int)

        tCounter = Counter(t)

        formed = 0
        req = len(tCounter)

        minL = float("inf")
        minWindow = (0,0)

        while right < len(s):


            right_char = s[right]
            freq[right_char] += 1

            if right_char in tCounter and freq[right_char] == tCounter[right_char]:
                formed += 1

            while left <= right and formed == req:
                 
                left_char = s[left]
                if right - left + 1 < minL:         
                    minL =  right - left + 1
                    minWindow = (left, right)
                

                freq[left_char] -= 1

                if left_char in tCounter and freq[left_char] < tCounter[left_char]:
                    formed -= 1
                left += 1

            right += 1
        
        if minL != float("inf"):
            return s[minWindow[0]:minWindow[1] + 1]
        
        return ""


