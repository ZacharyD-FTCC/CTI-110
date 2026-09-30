# Your Name
# September 30, 2026
# P2LAB2
# This program uses a dictionary to store vehicle MPG information
# and calculates the amount of gas needed for a given number of miles.

# Pseudocode:
# 1. Create a dictionary containing vehicles and their MPG.
# 2. Create a variable containing all the dictionary keys.
# 3. Display the vehicle keys.
# 4. Ask the user to enter a vehicle.
# 5. Display the MPG for the selected vehicle.
# 6. Ask the user how many miles they will drive.
# 7. Calculate gallons of gas needed.
# 8. Display the gallons needed rounded to two decimal places.

vehicles = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = vehicles.keys()

print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")

mpg = vehicles[vehicle]

print(f"The {vehicle} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {vehicle}: "))

gallons = miles / mpg

print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")