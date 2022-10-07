class ParkingSystem(object):
    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def add_car(self, car_type):
        match car_type:
            case 1:
                if self.big > 0:
                    self.big -= 1
                    return True
                else:
                    return False
            case 2:
                if self.medium > 0:
                    self.medium -= 1
                    return True
                else:
                    return False
            case 3:
                if self.small > 0:
                    self.small -= 1
                    return True
                else:
                    return False
            case _:
                return None

myLot = ParkingSystem(1, 1, 0)
print(myLot.add_car(3))