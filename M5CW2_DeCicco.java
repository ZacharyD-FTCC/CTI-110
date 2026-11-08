
import java.util.Scanner;

// Zachary DeCicco
// M5CW2
// Date: 11/07/2026
// This program collects five item prices, validates each price,
// and calculates the total cost and average price.

public class M5CW2_LastName {
    public static void main(String[] args) {

        // Create Scanner object
        Scanner input = new Scanner(System.in);

        // Variables
        double price;
        double total = 0;
        double average;
        int count = 1;

        // Do-While loop to collect five item prices
        do {
            System.out.print("Enter price for item #" + count + ": ");
            price = input.nextDouble();

            // While loop to validate the price
            while (price <= 0 || price > 10000) {
                System.out.println("Invalid price. Please enter a value between 0 and 10,000.");
                System.out.print("Enter price for item #" + count + ": ");
                price = input.nextDouble();
            }

            // Add valid price to total
            total += price;

            // Move to next item
            count++;

        } while (count <= 5);

        // Calculate average
        average = total / 5;

        // Display results
        System.out.println();
        System.out.println("All prices entered successfully!");
        System.out.printf("The total cost is: $%.2f%n", total);
        System.out.printf("The average price is: $%.3f%n", average);

        // Close Scanner
        input.close();
    }
}
