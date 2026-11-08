
import java.util.Scanner;

/**
 * M5HW1 - Updated Grade Calculator
 * Calculates the average of multiple grades
 * and determines the student's letter grade.
 */

public class M5HW1_DeCicco {

    public static void main(String[] args) {

        Scanner k = new Scanner(System.in);

        // Variables
        double average;
        double total;
        double gradeInput;
        int numGrades;
        int count;
        char grade;
        String repeat = "y";

        // Allow the program to run multiple times
        while (repeat.equalsIgnoreCase("y")) {

            total = 0;
            count = 1;

            // Ask how many grades the user wants to average
            System.out.print("How many grades would you like to enter? ");
            numGrades = k.nextInt();

            // Validate the number of grades
            while (numGrades <= 0) {
                System.out.println("Please enter at least one grade.");
                System.out.print("How many grades would you like to enter? ");
                numGrades = k.nextInt();
            }

            // Collect grades using a Do-While loop
            do {

                System.out.print("Enter grade #" + count + ": ");
                gradeInput = k.nextDouble();

                // Validate each grade using a While loop
                while (gradeInput < 0 || gradeInput > 100) {

                    System.out.println("Invalid grade. Please enter a value between 0 and 100.");

                    System.out.print("Enter grade #" + count + ": ");
                    gradeInput = k.nextDouble();
                }

                // Add valid grade to total
                total += gradeInput;

                // Move to next grade
                count++;

            } while (count <= numGrades);

            // Calculate average
            average = total / numGrades;

            System.out.printf("Average: %.1f%n", average);

            // Original if/else grading structure
            if (average >= 90) {
                grade = 'A';
            }
            else if (average >= 80) {
                grade = 'B';
            }
            else if (average >= 70) {
                grade = 'C';
            }
            else if (average >= 60) {
                grade = 'D';
            }
            else {
                grade = 'F';
            }

            // Display letter grade
            System.out.println("Letter Grade: " + grade);

            // Ask user if they want to run again
            System.out.print("\nWould you like to run the program again? (y/n): ");
            repeat = k.next();

        }

        // Exit message
        System.out.println("Program exited. Goodbye!");

        k.close();
    }
}
