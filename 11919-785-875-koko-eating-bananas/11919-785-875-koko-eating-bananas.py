class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:

            rate = left + ((right - left) // 2)

            time = 0

            for p in piles:
                time += math.ceil(p / rate)

            # print(f"l: {left} r: {right} rate: {rate} time: {time}")
            
            if time <= h:
                ans = rate
                right = rate - 1
            else:
                left = rate + 1
        
        return ans