
# Your Name
# 2026-10-12
# P3HW1 - Debugging
# This program collects six module grades and displays the lowest, highest,
# sum, average, and letter grade based on the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add the grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine the lowest, highest, sum, and average grades
low = min(grades)
high = max(grades)
grade_sum = sum(grades)
avg = grade_sum / len(grades)

# Display the results
print()
print(f'Lowest grade: {low:g}')
print(f'Highest grade: {high:g}')
print(f'Sum of grades: {grade_sum:g}')
print(f'Average: {avg:.2f}')

# Determine and display the letter grade for the average
if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f'Your grade is: {letter_grade}')

