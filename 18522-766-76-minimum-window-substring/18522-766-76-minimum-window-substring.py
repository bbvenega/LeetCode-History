class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""


        left = 0
        right = 0

        formed = 0
        freq = defaultdict(int)
        counter = Counter(t)
        req = len(counter)
        minL = float("inf")
        minWindow = (0, 0)


        while right < len(s):
            # print(f"Left: {left} Right: {right}")

            char = s[right]
            freq[char] += 1

            if char in counter and freq[char] == counter[char]:
                formed += 1

            while left <= right and formed == req:

                char = s[left]

                if right - left + 1 < minL:
                    minL = right - left + 1
                    minWindow = (left, right)

                freq[char] -= 1

                if char in counter and freq[char] < counter[char]:
                    formed -= 1

                left += 1

            right += 1

            # print(f"Freq is {freq}\n")

        return "" if minL == float("inf") else s[minWindow[0] : minWindow[1] + 1]
