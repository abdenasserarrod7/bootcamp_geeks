# ------ Exercise 1

# Ask the user to input a month (1 to 12)
month = int(input("Enter a month number (1-12): "))

# Determine the season
if 3 <= month <= 5:
    season = "Spring"
elif 6 <= month <= 8:
    season = "Summer"
elif 9 <= month <= 11:
    season = "Autumn"
elif month == 12 or month <= 2:
    season = "Winter"
else:
    season = "Invalid month"

# Display the result
print(f"The season is: {season}")


# ------ Exercise 2

# 1. Print numbers from 1 to 20
for num in range(1, 21):
    print(num)

print("---- Even index numbers ----")

# 2. Print numbers at even indexes
# Index starts from 0, so even index means index % 2 == 0
for index, num in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(num)


# ------ Exercise 3

my_name = "Nasser"

name = ""
while name != my_name:
    name = input("Enter your name: ")

print("You got it! That’s my name.")


# ------ Exercise 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    print("Index:", names.index(user_name))
else:
    print("Name not found.")


# ------ Exercise 5

# Ask the user for 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the greatest number
greatest = max(num1, num2, num3)

# Print the result
print("The greatest number is:", greatest)


# ------ Exercise 6

import random

wins = 0
losses = 0

while True:
    
    guess = input("Enter a number from 1 to 9 (or 'q' to quit): ").strip()
    
    if guess.lower() == 'q':
        break  

    if not guess.isdigit() or not (1 <= int(guess) <= 9):
        print("Invalid input. Please enter a number from 1 to 9.")
        continue

    guess = int(guess)
    number = random.randint(1, 9)

    if guess == number:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time. The correct number was {number}.")
        losses += 1


print(f"\nGame over! Wins: {wins}, Losses: {losses}")


# ------ Exercise 7

# ------ Exercise 8
