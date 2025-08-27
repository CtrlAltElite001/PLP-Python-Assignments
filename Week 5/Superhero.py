# Base Class: Superhero
class Superhero:
    def __init__(self, name, alias, power, city):
        self.name = name           # Real name
        self.alias = alias         # Superhero alias
        self._power = power        # Protected attribute (Encapsulation)
        self.city = city

    def introduce(self):
        return f"I am {self.alias}, protector of {self.city}!"

    def use_power(self):
        return f"{self.alias} uses {self._power}!"

    def get_power(self):
        """Encapsulated getter for power"""
        return self._power

    def set_power(self, new_power):
        """Encapsulated setter for power"""
        self._power = new_power


# Derived Class: FlyingHero (inherits from Superhero)
class FlyingHero(Superhero):
    def __init__(self, name, alias, power, city, flight_speed):
        super().__init__(name, alias, power, city)
        self.flight_speed = flight_speed

    # Polymorphism: Overriding the use_power method
    def use_power(self):
        return f"{self.alias} soars through the sky at {self.flight_speed} km/h using {self._power}!"


# Derived Class: TechHero (inherits from Superhero)
class TechHero(Superhero):
    def __init__(self, name, alias, power, city, gadgets):
        super().__init__(name, alias, power, city)
        self.gadgets = gadgets

    # Polymorphism: Overriding the introduce method
    def introduce(self):
        return f"{self.alias}, master of technology, defends {self.city} with {len(self.gadgets)} gadgets!"


# Example Usage
if __name__ == "__main__":
    hero1 = Superhero("Clark Kent", "Superman", "Super Strength", "Metropolis")
    hero2 = FlyingHero("Diana Prince", "Wonder Woman", "Divine Flight", "Themyscira", 1200)
    hero3 = TechHero("Tony Stark", "Iron Man", "Powered Armor", "New York", ["Repulsors", "Missiles", "AI"])

    # Base hero
    print(hero1.introduce())
    print(hero1.use_power())

    # FlyingHero (demonstrates polymorphism)
    print(hero2.introduce())
    print(hero2.use_power())

    # TechHero (demonstrates polymorphism + encapsulation)
    print(hero3.introduce())
    print(hero3.use_power())
    print("Iron Man’s Power:", hero3.get_power())
    hero3.set_power("Nanotech Armor")
    print("Iron Man’s New Power:", hero3.get_power())
