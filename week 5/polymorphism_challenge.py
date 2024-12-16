# polymorphism_challenge.py

# Base class
class Vehicle:
    def move(self):
        pass


# Subclasses
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
