from datetime import datetime

# Ask for birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

# Today's date
today = datetime.today()

# Calculate age
age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Number of candles = last digit of age
candles_count = age % 10
candles = "i" * candles_count

# Cake template
def print_cake(candles):
    print(f"       ___{candles}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

# Check for leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Display cakes
if is_leap_year(birthdate.year):
    print_cake(candles)
    print_cake(candles)
else:
    print_cake(candles)
