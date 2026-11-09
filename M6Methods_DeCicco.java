
import java.util.Scanner;

// Group project starter file
public class M6Methods_DeCicco
{
    static Scanner in = new Scanner(System.in);

    public static void main(String[] args)
    {
        runProgram();
    }

    public static void runProgram()
    {
        String keep_going = "yes";

        while (keep_going.equalsIgnoreCase("yes"))
        {
            displayMenu();

            System.out.println();
            System.out.println("You have exited the menu!");
            System.out.print("Do you want to see the menu again? Enter yes or no: ");

            keep_going = in.next();

            System.out.println();
        }

        System.out.println("Program has terminated.");
    }

    public static void displayMenu()
    {
        System.out.println();
        System.out.println("Menu");
        System.out.println("-------------------------");
        System.out.println("1) M6HW1");
        System.out.println("2) M6HW2");
        System.out.println("3) M6HW3");
        System.out.println("4) Exit");
        System.out.println();

        System.out.print("Selection: ");

        int selection = in.nextInt();

        switch (selection)
        {
            case 1:
                getM6HW1();
                displayMenu();
                break;

            case 2:
                System.out.println("-------------------------");
                System.out.println("You picked M6HW2");
                System.out.println("-------------------------");
                displayMenu();
                break;

            case 3:
                System.out.println("-------------------------");
                System.out.println("You picked M6HW3");
                System.out.println("-------------------------");
                displayMenu();
                break;

            case 4:
                System.out.println("-------------------------");
                System.out.println("Exiting the menu");
                break;

            default:
                System.out.println("-------------------------");
                System.out.println("Unrecognized option. Try again.");
                System.out.println("-------------------------");
                displayMenu();
                break;
        }
    }

    // Method for M6HW1
    public static void getM6HW1()
    {
        System.out.println("-------------------------");
        System.out.println("You picked M6HW1");
        System.out.println("-------------------------");

        // Add your M6HW1 assignment code here.
    }
}
