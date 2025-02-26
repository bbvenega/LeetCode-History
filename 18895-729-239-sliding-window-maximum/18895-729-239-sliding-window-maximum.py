class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        
        right = 0

        dq = deque()

        ans = []

        while right < len(nums):
            # print(f"dq before this cycle: {dq}")
            if dq and dq[0] < right - k + 1:
                dq.popleft()
            
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()

            
            dq.append(right)

            if dq and right + 1 >= k:
                ans.append(nums[dq[0]])
            # print(f"dq after this cycle: {dq}\n")
            right += 1
        return ans
