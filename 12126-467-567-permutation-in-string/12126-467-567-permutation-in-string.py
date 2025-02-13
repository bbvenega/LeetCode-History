class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Counter = Counter(s1)
        s2Counter = Counter(s2[:len(s1)])

        for right in range(len(s1), len(s2)):

            # print(f"s1: {s1Counter} and s2: {s2Counter}")
            if s1Counter == s2Counter:
                return True

            s2Counter[s2[right - len(s1)]] -= 1
            s2Counter[s2[right]] += 1

        return s1Counter == s2Counter 