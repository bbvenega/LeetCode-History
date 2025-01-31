class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #If either string is empty return empty string
        if not s or not t:
            return ""
        

        #Count the amount of characters necessary
        tCount = Counter(t)

        #The required length of the string
        req = len(tCount)

        
        #initialize left / right and a formed to track the len of current window
        left, right = 0, 0
        formed = 0

        # Will keep frequency of current window
        windowCounter = {}


        #initalize minimum left var
        minL = float("inf")

        #holds indices for smallest window
        minWindow = (0,0)

        while right < len(s):

            # get new char and incrememnt frequency count
            char = s[right]
            windowCounter[char] = windowCounter.get(char, 0) + 1

            #if it is a necessary char and the frequency of it in the window matches the amount necessary
            if char in tCount and windowCounter[char] == tCount[char]:
                #update window size
                formed += 1

            
            # while the window has all the required characters
            while left <= right and formed == req:
                char = s[left]

                #update the current window size and indices
                if right - left + 1 < minL:
                    minL = right - left + 1
                    minWindow = (left, right)

                #remove the left char from the window
                windowCounter[char] -= 1

                #if the removed char was necessary and now results missing characters
                #shrink the window
                if char in tCount and windowCounter[char] < tCount[char]:
                    formed -= 1
                
                left += 1

            right += 1

        #returns the string of min window
        return "" if minL == float("inf") else s[minWindow[0]:minWindow[1] + 1]
        



        