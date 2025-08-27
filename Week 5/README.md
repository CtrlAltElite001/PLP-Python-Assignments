# Object-Oriented Programming Challenges 🚀

This repository contains two Python programs that demonstrate **OOP concepts**:  
1. **Superhero Class** 🦸‍♂️ – Encapsulation, Inheritance, and Polymorphism  
2. **Polymorphism Challenge with Vehicles** 🎭 – Method overriding with different behaviors  

---

## 🦸 Superhero Class

### Features
- **Attributes**: `name`, `alias`, `power`, `city`
- **Encapsulation**: Power is a protected attribute (`_power`), accessed through getter/setter
- **Inheritance**: Subclasses `FlyingHero` and `TechHero` extend the base `Superhero` class
- **Polymorphism**: Methods like `introduce()` and `use_power()` are overridden in subclasses

### Example Code
```python
hero1 = Superhero("Clark Kent", "Superman", "Super Strength", "Metropolis")
hero2 = FlyingHero("Diana Prince", "Wonder Woman", "Divine Flight", "Themyscira", 1200)
hero3 = TechHero("Tony Stark", "Iron Man", "Powered Armor", "New York", ["Repulsors", "Missiles", "AI"])

print(hero1.introduce())   # Superman introduces himself
print(hero2.use_power())   # Wonder Woman uses flight
print(hero3.introduce())   # Iron Man shows off his gadgets
🎭 Polymorphism Challenge (Vehicles)
Concept

All vehicles share the same method move(), but each subclass defines it differently.

Example Code
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    print(v.move())


**## 🧑‍💻 How to Run**

1. Clone this repository or copy the code into a .py file.

2. Run the program using:
python filename.py
3. View the printed results in your terminal.

**## 📚 Concepts Covered**

Classes & Objects

Constructors (__init__)

Encapsulation (getter/setter methods)

Inheritance (base and derived classes)

Polymorphism (method overriding)
