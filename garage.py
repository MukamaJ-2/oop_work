class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def set_vehicle(self, parked):
        self.parked_vehicle = parked

    def __str__(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle}"
        else:
            return "Garage is empty"