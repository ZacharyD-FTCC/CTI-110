import java.util.Scanner;

public class M6CW2_DeCicco {

    // Main method controls the program and calls the other methods.
    public static void main(String[] args) {
        displayGreeting();
        calculateArea();
        displayClosing();
    }

    // Displays a welcome message.
    public static void displayGreeting() {
        System.out.println("Welcome to the Area Calculator!");
    }

    // Gets the rectangle's length and width and calculates its area.
    public static void calculateArea() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the length: ");
        double length = input.nextDouble();

        System.out.print("Enter the width: ");
        double width = input.nextDouble();

        double area = length * width;

        System.out.println("The area of the rectangle is " + area + ".");
    }

    // Displays the closing message.
    public static void displayClosing() {
        System.out.println("Thank you for using this program!");
    }
}
