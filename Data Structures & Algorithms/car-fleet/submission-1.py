class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)
        for i in range(n):
            cars.append([position[i], speed[i]])
        
        cars.sort(key = lambda x:x[0], reverse = True)

        fleet = 0 
        t_prev = float("-inf")

        for p,s in cars:
            t = (target - p) / s
            if t > t_prev:
                fleet += 1
                t_prev = t

        return fleet 

