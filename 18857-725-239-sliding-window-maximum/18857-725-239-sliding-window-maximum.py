class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []

        for right in range(len(nums)):
            # print(f"i: {right}Dq: {dq}")

            if dq and dq[0] < right - k + 1:
                
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

            if right >= k - 1:
                ans.append(nums[dq[0]])

            


        
        return ans
        