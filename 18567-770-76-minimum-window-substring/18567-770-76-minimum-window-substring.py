class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req = len(t)

        tCounter = Counter(t)
        freq = defaultdict(int)
        formed = 0

        left = 0
        right = 0

        minL = 1000000000
        minWindow = (0,0)

        while right < len(s):

            right_char = s[right]

            if right_char in tCounter and freq[right_char] < tCounter[right_char]:
                formed += 1
            
            freq[right_char] += 1
            while left <=  right and formed == req:
                # print(f"formed == req left: {left} and right {right}")

                left_char = s[left]
                freq[left_char] -= 1

                if(right - left + 1 < minL):
                    minL = right - left + 1
                    minWindow = (left, right)


                if left_char in tCounter and freq[left_char] < tCounter[left_char]:
                    formed -= 1

                
                left += 1

            right += 1

        if minL == 1000000000:
            return ""
        
        return s[minWindow[0]:minWindow[1] + 1]
                

                


