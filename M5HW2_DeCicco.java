import java.util.Scanner;

public class M5HW2_DeCicco {
    public static void main(String[] args) {

        // Zachary DeCicco
        // M5HW2
        // Date: 11/07/2026
        // This program calculates monthly widget sales,
        // returns, commission, and salary using loops.

        Scanner input = new Scanner(System.in);

        final double WIDGET_PRICE = 4.79;
        final double BASE_SALARY = 2000.00;

        String runAgain = "y";
        int month = 1;

        // While loop allows the program to run again
        while (runAgain.equalsIgnoreCase("y")) {

            System.out.print("Enter Sales Person Name: ");
            String name = input.nextLine();

            int totalWidgetsSold = 0;
            int totalWidgetsReturned = 0;

            // First for loop collects weekly widget sales
            System.out.println("\nEnter weekly widget sales:");

            for (int week = 1; week <= 4; week++) {
                System.out.print("Week " + week + " widgets sold: ");
                int weeklySales = input.nextInt();

                totalWidgetsSold += weeklySales;
            }

            // Second for loop collects weekly widget returns
            System.out.println("\nEnter weekly widget returns:");

            for (int week = 1; week <= 4; week++) {
                System.out.print("Week " + week + " widgets returned: ");
                int weeklyReturns = input.nextInt();

                totalWidgetsReturned += weeklyReturns;
            }

            // Calculate monthly totals
            int netWidgetsSold = totalWidgetsSold - totalWidgetsReturned;

            double widgetSalesAmount = netWidgetsSold * WIDGET_PRICE;

            // Determine commission rate
            double commissionRate;

            if (netWidgetsSold >= 0 && netWidgetsSold <= 100) {
                commissionRate = 0.10;
            }
            else if (netWidgetsSold >= 101 && netWidgetsSold <= 199) {
                commissionRate = 0.15;
            }
            else if (netWidgetsSold >= 200 && netWidgetsSold <= 300) {
                commissionRate = 0.20;
            }
            else {
                commissionRate = 0.25;
            }

            // Calculate commission and monthly salary
            double commissionAmount =
                    Math.round(widgetSalesAmount * commissionRate * 100.0) / 100.0;

            double monthlySalary = BASE_SALARY + commissionAmount;

            // Display monthly results
            System.out.println("\n--------------------------------");
            System.out.println("Sales Person: " + name);
            System.out.println("Month #" + month);
            System.out.println("Widgets Sold: " + totalWidgetsSold);
            System.out.println("Widgets Returned: " + totalWidgetsReturned);
            System.out.println("Net Widgets Sold: " + netWidgetsSold);

            System.out.printf("Widgets Sales Amount: %.2f%n", widgetSalesAmount);
            System.out.printf("Commission Amount: %.2f%n", commissionAmount);
            System.out.printf("Monthly Salary: %.2f%n", monthlySalary);

            System.out.println("--------------------------------");

            month++;

            // Ask user if they want to run the program again
            System.out.print("\nWould you like to run the program again? (y/n): ");
            runAgain = input.next();

            // Clear the input buffer
            input.nextLine();
        }

        System.out.println("\nProgram exited. Goodbye!");

        input.close();
    }
}