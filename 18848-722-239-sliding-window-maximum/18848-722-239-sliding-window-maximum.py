class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()
        ans = []
        left = 0
        right = 1
        while left < len(nums):
            

            # condition to adding to dq
            if dq and dq[0] < left - k + 1:
                dq.popleft()


            while dq and nums[dq[-1]] < nums[left]:
                dq.pop()
            
            dq.append(left)

            if left >= k - 1:
                ans.append(nums[dq[0]])

            left += 1


        return ans

