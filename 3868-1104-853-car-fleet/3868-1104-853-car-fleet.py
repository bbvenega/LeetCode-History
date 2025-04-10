class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p,s) for (p,s) in zip(position,speed)]

        pair.sort(reverse=True)
        print(f"Pairs: {pair}")

        fleet = []


        for p,s in pair:

            time = (target - p) / s
            # print(f"t: {time}")

            fleet.append(time)
            if len(fleet) > 1 and fleet[-2] >= fleet[-1]:
                fleet.pop()
            

        return len(fleet)