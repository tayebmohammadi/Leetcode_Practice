class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.garage = {}
        self.garage[1] = big
        self.garage[2] = medium
        self.garage[3] = small


    def addCar(self, carType: int) -> bool:
        if self.garage[carType] == 0:
            return False
        self.garage[carType] -= 1
        return True
