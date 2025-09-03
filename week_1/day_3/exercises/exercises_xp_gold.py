# ------ Exercise 1

import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        """Compute the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def area(self):
        """Compute the area of the circle."""
        return math.pi * (self.radius ** 2)

    def definition(self):
        """Print the geometrical definition of a circle."""
        print("A circle is the set of all points in a plane that are at a given distance (the radius) from a fixed point (the center).")


# Example usage:
c = Circle(3)
print("Perimeter:", c.perimeter())
print("Area:", c.area())
c.definition()


# ------ Exercise 2

import random

class MyList:
    def __init__(self, letters: list):
        self.letters = letters

    def get_reversed(self):
        """Return the reversed list"""
        return self.letters[::-1]

    def get_sorted(self):
        """Return the sorted list"""
        return sorted(self.letters)

    def generate_random_list(self):
        """Generate a random list of integers with the same length"""
        return [random.randint(0, 100) for _ in range(len(self.letters))]


# Example usage:
mylist = MyList(['d', 'a', 'c', 'b'])

print("Original list:", mylist.letters)
print("Reversed list:", mylist.get_reversed())
print("Sorted list:", mylist.get_sorted())
print("Random list:", mylist.generate_random_list())


# ------ Exercise 3

# menu_manager.py

class MenuManager:
    def __init__(self):
        # Initial menu setup
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        """Add a new dish to the menu."""
        self.menu.append({
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        })
        print(f"✅ {name} has been added to the menu.")

    def update_item(self, name, price, spice, gluten):
        """Update an existing dish if found."""
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"🔄 {name} has been updated.")
                return
        print(f"⚠️ {name} is not in the menu.")

    def remove_item(self, name):
        """Remove a dish if it exists."""
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f"❌ {name} has been removed. Updated menu:")
                print(self.menu)
                return
        print(f"⚠️ {name} is not in the menu.")


# ------ Exercise 4

# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
