class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # intitalize binary search with left as 1 and right as the biggest pile
        # Also, set answer as your max pile length by default as the worst case
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            
            # Set the banana per hour rate to the midpoint in the BS
            k = l +((r - l) // 2)

            #Initalize the total time for this iteration of k
            totalTime = 0

            # For every pile, set the time equal the the pile size divided by the banana per hour rate
            # This math adds how many hours it takes to finish the pile given K
            for p in piles:
                totalTime += math.ceil(float(p) / k)

            # If the total time to finish every pile was less than the max amount of hours, we can try a
            # smaller K
            if totalTime <= h:
                ans = k
                r = k - 1

            # If the total time to finish every pile was greater than the max amount of hours, we can try a 
            # larger K    
            else:
                l = k + 1
        
        return ans