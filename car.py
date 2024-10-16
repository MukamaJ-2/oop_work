from vehicle import * 
class Car(Vehicle):
    def __init__(self, color,has_winter_tires =False):
        super().__init__(color)
        self._has_winter_tires = has_winter_tires
    
    def __str__(self):
        return (super().__str__() + f"\n has winter tires: {self._has_winter_tires}")

car1 =Car("Black")
print(car1)