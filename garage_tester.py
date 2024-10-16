from truck import Truck
from garage import Garage

class GarageTester:
    @staticmethod
    def get_example():
        truck = Truck("black")
        garage = Garage()
        garage.set_vehicle(truck)
        return garage