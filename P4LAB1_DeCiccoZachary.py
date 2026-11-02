
# Zachary
# Date: November 1, 2026
# Assignment: P4LAB1
# Description: This program uses turtle graphics to draw a house
#              using a square and a triangle.

# Pseudocode:
# 1. Import the turtle library.
# 2. Create the drawing window and turtle.
# 3. Change the background and turtle colors.
# 4. Position the turtle to draw the square.
# 5. Use a while loop to draw four sides of the square.
# 6. Position the turtle to draw the roof.
# 7. Use a for loop to draw three sides of the triangle.
# 8. Hide the turtle and keep the window open.

import turtle

# Create the window
window = turtle.Screen()
window.title("P4LAB1 - Turtle House")
window.bgcolor("lightblue")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.pencolor("saddlebrown")
t.pensize(5)
t.speed(4)

# Draw the square using a while loop
t.penup()
t.goto(-100, -100)
t.setheading(0)
t.pendown()

side = 200
count = 0

while count < 4:
    t.forward(side)
    t.left(90)
    count += 1

# Draw the triangle using a for loop
t.penup()
t.goto(-100, 100)
t.setheading(0)
t.pendown()

for side_number in range(3):
    t.forward(side)
    t.left(120)

# Hide the turtle
t.hideturtle()

# Keep the window open
window.mainloop()
