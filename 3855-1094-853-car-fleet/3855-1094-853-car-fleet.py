class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p,s) for (p,s) in (zip(position, speed))]
        # print(pair)
        

        pair.sort(reverse=True)
        # print(pair)

        stack = [] 

        for p,s in pair:

            t = (target - p) / s
            # print(t)

            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)