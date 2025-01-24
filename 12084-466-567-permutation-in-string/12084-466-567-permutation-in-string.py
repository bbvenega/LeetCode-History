class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = len(s1) -1

        sorteds1 = ''.join(sorted(s1))
        while right < len(s2):
            # print(f"left: {left} right: {right}")
            temp = s2[left:right + 1]

            sortedTemp = ''.join(sorted(temp))
            # print(f"comparing temp: {temp}, sorted to {sortedTemp} to sortedS1 {sorteds1}")

            if sortedTemp == sorteds1:
                return True
            
            left += 1
            right += 1

        return False