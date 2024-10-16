# vehicle.py

class Vehicle:
    def __init__(self, color):
        self._color = color
    

    def get_color(self):
        return self._color
        
    
    def __str__(self):
        return f"This vehicle is {self._color}"
    
#vehicle1 = Vehicle("red")
#print(vehicle1)