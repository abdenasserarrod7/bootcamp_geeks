# ------ Exercise 1

print("Hello world\n" * 4, end="")

# ------ Exercise 2

calc = (99 ** 3) * 8
print(calc)

# ------ Exercise 3

my_name = "Nasser"

username = input("Enter your username: ")

if (username == my_name):
    print("Woah we have the same name  " + username + "!")
else:
    print("You don't have my name but you have a beautiful name, " + username + "!")

# ------ Exercise 4

height_cm = int(input("Please enter your height in centimeters: "))

if height_cm > 145 :
    print("You are tall enough to ride the roller coaster!")
else:
    print("Sorry, you need to be taller to ride the roller coaster.")


# ------ Exercise 5

my_fav_numbers = {0, 1, 7 , 10}
print("My favorite numbers:", my_fav_numbers)

my_fav_numbers.add(18)
my_fav_numbers.add(25)
print("After adding two numbers:", my_fav_numbers)

my_fav_numbers.remove(25)
print("After removing one number:", my_fav_numbers)

friend_fav_numbers = {4, 9, 15}
print("Friend's favorite numbers:", friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

# ------ Exercise 6

t = (1, 2, 3)

t = t + (4, 5)  
print(t)

# ------ Exercise 7

basket = ["Banana", "Apples", "Oranges", "Blueberries"]


basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

apple_count = basket.count("Apples")
print("Number of apples:", apple_count)

print(basket)

basket.clear()

# ------ Exercise 8

sandwich_orders = [
    "Tuna sandwich",
    "Pastrami sandwich",
    "Avocado sandwich",
    "Pastrami sandwich",
    "Egg sandwich",
    "Chicken sandwich",
    "Pastrami sandwich"
]

print("Sorry, the deli has run out of Pastrami!\n")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print(sandwich_orders)

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich.lower()}.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

