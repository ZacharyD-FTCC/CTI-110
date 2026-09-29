# Your Name
# September 29, 2026
# P2HW2 - Lists and Grades
# This program collects six module grades, stores them in a list,
# and calculates the lowest grade, highest grade, sum, and average.

# Pseudocode:
# 1. Ask the user to enter a grade for each of the six modules.
# 2. Store the six grades in a list.
# 3. Find the lowest grade in the list.
# 4. Find the highest grade in the list.
# 5. Find the sum of all grades in the list.
# 6. Calculate the average of the grades.
# 7. Display the results with the required formatting.

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

print()
print("-------------Results----------------")
print(f"Lowest Grade:       {lowest_grade:.1f}")
print(f"Highest Grade:      {highest_grade:.1f}")
print(f"Sum of Grades:      {sum_grades:.1f}")
print(f"Average:            {average_grade:.2f}")
print("-------------------------------------")