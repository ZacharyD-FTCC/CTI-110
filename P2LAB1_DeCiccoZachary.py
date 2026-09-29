# Your Name
# September 29, 2026
# P2LAB1 - Circle
# This program calculates the diameter, circumference, and area of a circle.

# Pseudocode:
# 1. Ask the user to enter the radius of the circle.
# 2. Convert the radius to a float.
# 3. Calculate the diameter using 2 * radius.
# 4. Calculate the circumference using 2 * pi * radius.
# 5. Calculate the area using pi * radius squared.
# 6. Display the diameter, circumference, and area with the required formatting.

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")