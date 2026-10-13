
# Your Name
# October 12, 2026
# P3HW2 - Employee Pay
# This program calculates an employee's regular pay, overtime pay, and gross pay.

# Pseudocode:
# 1. Ask the user to enter the employee's name.
# 2. Ask the user to enter the number of hours worked.
# 3. Ask the user to enter the employee's pay rate.
# 4. Determine whether the employee worked overtime.
# 5. If hours worked are greater than 40:
#       Calculate overtime hours.
#       Calculate regular pay for 40 hours.
#       Calculate overtime pay at 1.5 times the regular rate.
#    Else:
#       Set overtime hours and overtime pay to zero.
#       Calculate regular pay using hours worked.
# 6. Calculate gross pay by adding regular pay and overtime pay.
# 7. Display the employee's information and pay calculations.

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_rate = pay_rate * 1.5
    overtime_pay = overtime_hours * overtime_rate
    regular_pay = regular_hours * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("------------------------------------------")
print(f"Employee name:          {employee_name}")
print()
print(f"{'Hours Worked':<22}{'Pay Rate':<15}"
      f"{'Overtime':<15}{'Overtime Pay':<18}"
      f"{'RegHour Pay':<15}{'Gross Pay'}")
print("-" * 100)
print(f"{hours_worked:<22.2f}${pay_rate:<14.2f}"
      f"{overtime_hours:<15.2f}${overtime_pay:<17.2f}"
      f"${regular_pay:<14.2f}${gross_pay:.2f}")
print("------------------------------------------")
