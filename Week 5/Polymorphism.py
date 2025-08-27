# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"


class Bike(Vehicle):
    def move(self):
        return "🚴 Pedaling through the street"


# Demonstration of Polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Bike()]

    print("🚦 Vehicle Movements:")
    for v in vehicles:
        print(v.move())
