
# Zachary
# November 1, 2026
# P4LAB2
# This program displays a multiplication table for a non-negative integer
# and allows the user to run the program again.

# PSEUDOCODE:
# 1. Set the run-again response to "yes" so the program starts.
# 2. While the run-again response is "yes":
#    a. Ask the user to enter an integer.
#    b. If the integer is greater than or equal to zero:
#       i. Use a for loop to count from 1 through 12.
#       ii. Multiply the entered integer by the current loop number.
#       iii. Display the multiplication equation and result.
#    c. Otherwise, display a message that negative numbers are not accepted.
#    d. Ask the user whether they want to run the program again.
# 3. If the user enters "no", the while loop ends.
# 4. Display the program exit message.

run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter an integer: "))

    if number >= 0:
        for multiplier in range(1, 13):
            result = number * multiplier
            print(f"{number} * {multiplier} = {result}")
    else:
        print("This program does not handle negative number:")

    run_again = input("Would you like to run the program again? ")

print("Exiting program...")
