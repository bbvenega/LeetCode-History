class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s2Counter = Counter(s1)
        windowCounter = Counter(s2[:len(s1)])
        # print(f"s2Counter Counter is : {s2Counter}")


        for i in range(len(s2) - len(s1)):
            # print(f"i is {i} i + len(s1)")
            # print(f"Window Counter is : {windowCounter}\n")


            if windowCounter == s2Counter:
                return True
            
            windowCounter[s2[i]] -= 1

            if windowCounter[s2[i]] == 0:
                del windowCounter[s2[i]]

            windowCounter[s2[i+len(s1)]] += 1

        return windowCounter == s2Counter
