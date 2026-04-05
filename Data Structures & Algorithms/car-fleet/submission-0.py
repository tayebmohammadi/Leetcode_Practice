class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            t = (target - position[i])/speed[i]
            cars.append([position[i], t])

        cars.sort(key=lambda x: x[0], reverse=True)

        
        fleets = 0
        maxT = 0.0

        for _, t in cars:
            if t > maxT:
                fleets += 1
                maxT = t
            
        return fleets
