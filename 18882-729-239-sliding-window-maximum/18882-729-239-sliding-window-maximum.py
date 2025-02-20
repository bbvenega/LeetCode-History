class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()

        ans = []
        for right in range(len(nums)):



            # condition: pop while current right value is greater than last value in dq window
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()
            
            # condition: pop if current window indx is greater than last value in dq
            # print(f"Checking window idx: {right - k + 1}")
            if dq and right - k + 1 > dq[0]:
                dq.popleft()

            dq.append(right)

            if right - k + 1 >= 0:
                ans.append(nums[dq[0]])

            # if dq:
            #     print(f"{right}: dq[0]: {dq[0]} and dq[-1]: {dq[-1]}")
            #     print(f"{dq}\n")

        
        return ans