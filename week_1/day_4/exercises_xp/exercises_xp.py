# ------ Exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# ✅ New Siamese class inheriting from Cat
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# ✅ Create 3 cat instances
bengal_cat = Bengal("Leo", 2)
chartreux_cat = Chartreux("Milo", 3)
siamese_cat = Siamese("Luna", 1)

# ✅ List of all cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# ✅ Sara’s pets
sara_pets = Pets(all_cats)

# ✅ Take all cats for a walk
sara_pets.walk()


# ------ Exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}!"
        elif self_power < other_power:
            return f"{other_dog.name} wins the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"


# Create 3 dogs
dog1 = Dog("Buddy", 4, 20)
dog2 = Dog("Max", 6, 25)
dog3 = Dog("Rocky", 3, 30)

# Demonstration
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"{dog1.name}'s speed: {dog1.run_speed():.2f}")
print(f"{dog2.name}'s speed: {dog2.run_speed():.2f}")
print(f"{dog3.name}'s speed: {dog3.run_speed():.2f}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))


# ------ Exercise 3

# petdog.py

import random
from dog import Dog   # assuming your Dog class is in dog.py

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())  # use Dog's bark method
        self.trained = True

    def play(self, *dog_names):
        names = ", ".join(dog_names)
        print(f"{names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")


# ------ Exercise 4

class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []

    def born(self, **kwargs):
        """Add a child to the family members list."""
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        """Check if a family member is over 18 years old."""
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        print(f"No family member named {name} was found.")
        return False

    def family_presentation(self):
        """Print the family's last name and all members' details."""
        print(f"\nThe {self.last_name} Family Presentation:")
        for member in self.members:
            print(member)


# Create an instance of the Family class
members_list = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family("Smith", members_list)

# Test methods
my_family.family_presentation()

print("\nIs Michael over 18?", my_family.is_18("Michael"))
print("Is Sarah over 18?", my_family.is_18("Sarah"))

# Add a child
my_family.born(name="Emma", age=2, gender="Female", is_child=True)

# Present family again
my_family.family_presentation()


# ------ Exercise 5

class Family:
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self.members = members

    def family_presentation(self):
        print(f"Family {self.last_name} presentation:")
        for member in self.members:
            print(member)

    def born(self, **kwargs):
        """Adds a new member (baby) to the family"""
        self.members.append(kwargs)


class TheIncredibles(Family):
    def __init__(self, last_name, members=[]):
        super().__init__(last_name, members)

    def use_power(self, name):
        """Print the power of a member if they are over 18, otherwise raise an exception"""
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    print(f"{member['name']} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old, cannot use power!")
                return
        print(f"No member named {name} found.")

    def incredible_presentation(self):
        print("\n* Here is our powerful family *")
        super().family_presentation()


# --- Create the Incredibles instance ---
incredibles = TheIncredibles("Incredibles", [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
])

# Call incredible_presentation
incredibles.incredible_presentation()

# Use the born method to add Baby Jack
incredibles.born(
    name="Jack",
    age=1,
    gender="Male",
    is_child=True,
    power="Unknown Power",
    incredible_name="Baby Jack"
)

# Call incredible_presentation again
incredibles.incredible_presentation()


# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
