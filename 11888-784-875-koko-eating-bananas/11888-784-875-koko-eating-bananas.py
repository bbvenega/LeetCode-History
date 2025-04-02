class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)
        ans = r
        while l <= r:

            rate = l + ((r - l) // 2)
            time = 0

            for p in piles:
                time += math.ceil(float(p) / rate)

            # print(f"H: {h}, l: {l} and r: {r}, rate: {rate} time: {time}")
            
            if time <= h:
                ans = rate
                r = rate - 1
            else:
                l = rate + 1
        

        return ans
