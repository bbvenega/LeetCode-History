class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        ans = right

        while left <= right:

            time = 0
            rate = left + ((right - left) // 2)

            for p in piles:
                b = math.ceil(p / rate)
                time += b
            
            if time > h:
                left = rate + 1
            else:
                ans = rate
                right = rate - 1

        return ans