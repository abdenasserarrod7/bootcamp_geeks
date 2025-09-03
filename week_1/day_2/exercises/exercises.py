# ------ Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

# ------ Exercise 2

age = int(input("Enter your age: "))

if age < 3:
    price = 0
elif 3 <= age <= 12:
    price = 10
else:  # age > 12
    price = 15

print(f"Your ticket price is ${price}.")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name.title()} has to pay ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")


# ------ Exercise 3

# 1. Create the dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 2. Change the number of stores to 2
brand["number_stores"] = 2

# 3. Use the key type_of_clothes to print a sentence about clients
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")

# 4. Add country_creation
brand["country_creation"] = "Spain"

# 5. Check and add Desigual if key exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6. Delete creation_date
del brand["creation_date"]

# 7. Print the last international competitor
print(brand["international_competitors"][-1])

# 8. Print US major colors
print(brand["major_color"]["US"])

# 9. Print number of key-value pairs
print(len(brand))

# 10. Print the keys
print(brand.keys())

# 11. Create more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 12. Update brand with more_on_zara
brand.update(more_on_zara)

# 13. Print the value of number_stores
print(brand["number_stores"])  # It becomes 10000 because .update() overwrote the previous value


# ------ Exercise 4

def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Calling the function
describe_city("Reykjavik")            # Uses default country
describe_city("Akureyri")             # Uses default country
describe_city("Tokyo", "Japan")       # Overrides default country


# ------ Exercise 5

import random

def guess_number(num):
    r = random.randint(1, 100)
    print("🎉 Success!" if num == r else f"❌ Fail! You: {num}, Random: {r}")

guess_number(42)


# ------ Exercise 6

# Initial version
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

# Calling the function
make_shirt("Small", "Keep Calm and Code On")


# Modified version with defaults
def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

# 1. Large shirt with default message
make_shirt()

# 2. Medium shirt with default message
make_shirt("Medium")

# 3. Any size with different message
make_shirt("Small", "Code All Day!")

# Bonus: Using keyword arguments
make_shirt(text="Eat, Sleep, Code, Repeat", size="XL")


# ------ Exercise 7

import random

def get_random_temp(season):
    """Return a random temperature based on the given season."""
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(5, 23), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(10, 24), 1)
    else:
        raise ValueError("Invalid season.")

def get_season_from_month(month):
    """Return the season name based on the month number."""
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"
    else:
        raise ValueError("Month must be between 1 and 12.")

def main():
    try:
        month = int(input("Enter the month number (1 = Jan, 12 = Dec): "))
        season = get_season_from_month(month)
        
        temp = get_random_temp(season)
        print(f"The temperature right now is {temp}°C.")

        if temp < 0:
            print("Brrr, that's freezing! Wear some extra layers today.")
        elif 0 <= temp <= 16:
            print("Quite chilly! Don't forget your coat.")
        elif 17 <= temp <= 23:
            print("Nice weather — maybe take a walk outside.")
        elif 24 <= temp <= 32:
            print("Warm and pleasant — perfect for outdoor fun.")
        elif 33 <= temp <= 40:
            print("It's really hot! Stay hydrated.")
        else:
            print("Temperature out of expected range.")
    except ValueError as e:
        print(f"Error: {e}")

# Run the program
main()


# ------ Exercise 8
