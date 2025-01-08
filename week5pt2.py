class Transport:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Transport):
    def move(self):
        print("Driving 🚗")

class Plane(Transport):
    def move(self):
        print("Flying ✈️")

# Demonstration
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    
    car.move()   # Output: Driving 🚗
    plane.move() # Output: Flying ✈️
