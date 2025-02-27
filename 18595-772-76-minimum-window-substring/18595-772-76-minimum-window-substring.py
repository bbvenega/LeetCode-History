class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCounter = Counter(t)

        freq = defaultdict(int)

        formed = 0
        req = len(t)

        left = 0

        minWin = (0,0)
        minL = float("inf")

        for right in range(len(s)):

            right_char = s[right]

            if right_char in tCounter and freq[right_char] < tCounter[right_char]:
                formed += 1

            freq[right_char] += 1


            while left <= right and formed == req:
                print(f"we can shrink left since formed == req, current win {left} and {right}")
                left_char = s[left]

                freq[left_char] -= 1

                if right - left < minL:
                    minL = right - left
                    minWin = (left,right)

                if left_char in tCounter and freq[left_char] < tCounter[left_char]:
                    print(f"Had to decrement formed!")
                    formed -= 1

                left += 1
        
        if minL == float("inf"):
            return "" 
        return s[minWin[0]:minWin[1]+1]

