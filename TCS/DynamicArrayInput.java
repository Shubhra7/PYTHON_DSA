import java.util.ArrayList;
import java.util.Scanner;

public class DynamicArrayInput {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();

        String line = sc.nextLine();  // Read entire line
        String[] numbers = line.split(" ");  // Split by space
        
        for (String num : numbers) {
            list.add(Integer.parseInt(num));  // Convert to int and store
        }
        
        System.out.println("Your array is: " + list);
        sc.close();
    }
}
