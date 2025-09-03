# ------ Exercise 1

# Original string
manufacturers_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert to list (not by hand, but by splitting)
manufacturers = [m.strip() for m in manufacturers_str.split(",")]

# 1. Print how many manufacturers are in the list
print(f"There are {len(manufacturers)} manufacturers in the list.")

# 2. Print the list in reverse/descending order (Z-A)
manufacturers_desc = sorted(manufacturers, reverse=True)
print("Manufacturers in reverse order (Z-A):", manufacturers_desc)

# 3. Count how many have the letter 'o' in them
count_with_o = sum(1 for m in manufacturers if "o" in m.lower())
print(f"Manufacturers with the letter 'o': {count_with_o}")

# 4. Count how many do NOT have the letter 'i'
count_without_i = sum(1 for m in manufacturers if "i" not in m.lower())
print(f"Manufacturers without the letter 'i': {count_without_i}")

# BONUS: Duplicates list
manufacturers_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Remove duplicates using a set, then convert back to list
unique_manufacturers = list(set(manufacturers_with_duplicates))
print(f"Unique companies ({len(unique_manufacturers)} total): {', '.join(unique_manufacturers)}")

# BONUS: List in ascending order (A-Z) but reverse letters in each name
asc_reversed_letters = [m[::-1] for m in sorted(unique_manufacturers)]
print("A-Z order with reversed letters:", asc_reversed_letters)


# ------ Exercise 2

def get_full_name(first_name, last_name, middle_name=None):
    # Capitalize each provided name
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    if middle_name:
        middle_name = middle_name.capitalize()
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"


# Examples:
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))  # John Hooker Lee
print(get_full_name(first_name="bruce", last_name="lee"))  # Bruce Lee


# ------ Exercise 3

# ------ Exercise 4

# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
