# Zacahry
# 11/01/2026
# P4HW2
# This program calculates regular pay, overtime pay, and gross pay
# for multiple employees and displays totals for all employees.

"""
PSEUDOCODE

1. Initialize employee count and all pay totals to zero.
2. Ask the user to enter an employee name or "Done".
3. While the employee name is not "Done":
   a. Ask for hours worked.
   b. Ask for pay rate.
   c. If hours worked are greater than 40:
      - Calculate regular hours as 40.
      - Calculate overtime hours as hours worked minus 40.
   d. Otherwise:
      - Regular hours equal hours worked.
      - Overtime hours equal zero.
   e. Calculate regular pay.
   f. Calculate overtime pay using 1.5 times the pay rate.
   g. Calculate gross pay.
   h. Add employee pay to the running totals.
   i. Increase employee count by one.
   j. Display employee pay information.
   k. Ask for the next employee name.
4. When the user enters "Done":
   a. Display total employees entered.
   b. Display total overtime pay.
   c. Display total regular pay.
   d. Display total gross pay.
"""

# Initialize totals
employee_count = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Get employee name
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Process employees
while employee_name != "Done":

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate hours
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Update totals
    employee_count += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    # Display employee information
    print(f"\nEmployee name:   {employee_name}")
    print()

    print(f"{'Hours Worked':<16}{'Pay Rate':<13}{'OverTime':<13}"
          f"{'OverTime Pay':<22}{'RegHour Pay':<22}{'Gross Pay':>12}")

    print("-" * 99)

    print(f"{hours_worked:<16.1f}{pay_rate:<13.2f}{overtime_hours:<13.1f}"
          f"${overtime_pay:<21,.2f}${regular_pay:<21,.2f}${gross_pay:>11,.2f}")

    print()

    # Get next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Display final totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:,.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:,.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:,.2f}")