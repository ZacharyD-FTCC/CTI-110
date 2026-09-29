# Your Name
# September 29, 2026
# P2HW1 - Travel Expenses
# This program calculates and displays travel expenses and the remaining balance.

# Pseudocode:
# 1. Ask the user to enter their initial budget.
# 2. Ask the user to enter their travel destination.
# 3. Ask the user to enter the amount they expect to spend on fuel.
# 4. Ask the user to enter the amount they expect to spend on accommodation/hotel.
# 5. Ask the user to enter the amount they expect to spend on food.
# 6. Calculate the remaining balance.
# 7. Display the travel expense information with proper formatting.

print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
fuel = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

remaining_balance = budget - fuel - accommodation - food

print("\n" + "-" * 24 + "Travel Expenses" + "-" * 24)

print("{:<20}{:>20}".format("Location:", destination))
print("{:<20}${:>19.2f}".format("Initial Budget:", budget))
print("{:<20}${:>19.2f}".format("Fuel:", fuel))
print("{:<20}${:>19.2f}".format("Accommodation:", accommodation))
print("{:<20}${:>19.2f}".format("Food:", food))

print("-" * 64)
print("{:<20}${:>19.2f}".format("Remaining Balance:", remaining_balance))