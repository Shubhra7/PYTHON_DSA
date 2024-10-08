import java.util.Scanner;

public class Reverse_String {
    public static void reverse(char arr[], int i, int n) {
        if (i >= n / 2)
            return;
        char temp = arr[i];
        arr[i] = arr[n - i - 1]; // swapping first and last pointer index
        arr[n - i - 1] = temp;

        reverse(arr, i + 1, n);

    }

    public static char[] recur_rev(char arr[]) {
        reverse(arr, 0, arr.length);
        return arr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String: ");
        String st = sc.nextLine();
        
        char[] arr = st.toCharArray();
        
        String reverse_St = new String(recur_rev(arr));
        System.out.println(reverse_St);

        sc.close();
    }

}
