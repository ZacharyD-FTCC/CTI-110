
# Your Name
# 11/01/2026
# P4HW1
# This program collects test scores, validates them,
# drops the lowest score, calculates the average,
# and displays the corresponding letter grade.

# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store the scores.
# 3. Use a for loop to collect each score.
# 4. Use a while loop to make sure each score is between 0 and 100.
# 5. If a score is invalid, ask the user to enter it again.
# 6. Add each valid score to the score list.
# 7. Find and display the lowest score.
# 8. Remove the lowest score from the list.
# 9. Display the modified score list.
# 10. Calculate and display the average.
# 11. Determine and display the letter grade.

# Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list for scores
scores = []

# Loop to collect scores
for i in range(num_scores):

    score = float(input(f"Enter score #{i + 1}: "))

    # Validate the score
    while score < 0 or score > 100:
        print("Invalid score entered!!!!")
        print("Score should be between 0 and 100")

        score = float(input(f"Enter score #{i + 1} again: "))

    # Add valid score to the list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

# Remove the lowest score
scores.remove(lowest_score)

# Calculate the average of the remaining scores
average = sum(scores) / len(scores)

# Determine the letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List: {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {letter_grade}")
print("--------------------------------")
