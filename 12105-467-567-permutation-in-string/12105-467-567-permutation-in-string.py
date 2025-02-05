class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        left = 0
        

        s1_count = Counter(s1)
        windowCount = Counter(s2[:len(s1)])
        # print(f"windowCount: {windowCount}")

        for i in range(len(s1), len(s2)):
            if s1_count == windowCount:
                return True
            windowCount[s2[i]] += 1
            leftCh = s2[i-len(s1)]
            windowCount[leftCh] -= 1
            # print(f"Checking window {left} and {i}, substr: {s2[left:i+1]}")
            # print(f"s1_count: {s1_count}\n")

            

            if s1_count[leftCh] < 1:
                del s1_count[leftCh]

            
            
        return s1_count == windowCount
        
        


