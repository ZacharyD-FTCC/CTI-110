# Zachary DeCicco
# October 12, 2026
# P3LAB - Change Calculator
# This program calculates the dollars and coins needed to make change.

# Pseudocode:
# Ask the user to enter an amount of money.
# Convert the amount to an integer number of cents.
# Calculate the number of dollars.
# Calculate the number of quarters.
# Calculate the number of dimes.
# Calculate the number of nickels.
# Calculate the number of pennies.
# Display only denominations that are needed.
# Use singular or plural denomination names as appropriate.

# Get the amount of money from the user.
amount = float(input("Enter the amount of money: $"))

# Convert the amount to cents.
cents = round(amount * 100)

# Calculate dollars.
dollars = cents // 100
cents = cents % 100

# Calculate quarters.
quarters = cents // 25
cents = cents % 25

# Calculate dimes.
dimes = cents // 10
cents = cents % 10

# Calculate nickels.
nickels = cents // 5
cents = cents % 5

# Remaining cents are pennies.
pennies = cents

# Display the change, using singular and plural names.
if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")