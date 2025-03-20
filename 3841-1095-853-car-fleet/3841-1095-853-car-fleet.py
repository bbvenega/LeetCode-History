class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        # Create a pair array of all the positions and speeds
        pair = [(p,s) for p,s in zip(position, speed)]

        # sort the pair array in reverse order, putting the farthest starting position first
        pair.sort(reverse = True)

        #stack to keep track of fleets
        stack = []

        # for everythin in pair
        for p,s in pair:

            # get the time that it will take for it to arrive at the target 
            stack.append((target - p) / s)

            # if the stack has 2 or more fleets and the most recent inserted time is less than or equal to the fleet before it,
            # then it caught up: you can pop
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

