class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        pair = [(p,s) for (p,s) in zip(position, speed)]

        pair.sort(reverse=True)

        for p,s in pair:
            time = (target - p) / s

            # print(f"time: {time}")

            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()


        return len(stack) 