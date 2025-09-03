# ------ Exercise 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Instantiate three Cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 2)


# Function to find the oldest cat
def find_oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)


# Use the function to find the oldest
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Print result
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


# ------ Exercise 2

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


# Create David's dog
davids_dog = Dog("Rex", 50)
print(f"David's dog name: {davids_dog.name}, height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

# Create Sarah's dog
sarahs_dog = Dog("Teacup", 20)
print(f"\nSarah's dog name: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Check which dog is bigger
if davids_dog.height > sarahs_dog.height:
    print(f"\nThe bigger dog is {davids_dog.name}")
elif sarahs_dog.height > davids_dog.height:
    print(f"\nThe bigger dog is {sarahs_dog.name}")
else:
    print("\nBoth dogs are the same size")


# ------ Exercise 3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Create an object
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Call the method
stairway.sing_me_a_song()


# ------ Exercise 4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        """Add a new animal if it’s not already in the zoo."""
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to {self.name}.")
        else:
            print(f"{new_animal} is already in the zoo!")

    def get_animals(self):
        """Print all animals currently in the zoo."""
        print(f"Animals in {self.name}: {self.animals}")

    def sell_animal(self, animal_sold):
        """Remove an animal if it exists in the zoo."""
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.name}.")
        else:
            print(f"{animal_sold} is not in {self.name}.")

    def sort_animals(self):
        """Sort and group animals by their starting letter."""
        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)

        # Convert single-element lists to just the string (for nicer format)
        for key in grouped_animals:
            if len(grouped_animals[key]) == 1:
                grouped_animals[key] = grouped_animals[key][0]

        return grouped_animals

    def get_groups(self):
        """Print the grouped animals."""
        groups = self.sort_animals()
        print("Animal groups:")
        for key, value in groups.items():
            print(f"{key}: {value}")


# Example usage
new_york_zoo = Zoo("New York Zoo")

new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Ape")

new_york_zoo.get_animals()
new_york_zoo.sell_animal("Bear")
new_york_zoo.get_animals()

new_york_zoo.get_groups()


# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
