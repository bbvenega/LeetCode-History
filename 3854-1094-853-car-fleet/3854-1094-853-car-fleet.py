class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)

        for p,s in pair:

        
            time = (target - p) / s

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            

        return len(stack)