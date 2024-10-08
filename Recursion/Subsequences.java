import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

// Subsequences ==> a contiguous/ non-contiguious sequences, which follows the **order**
// Striver video => 6

public class Subsequences {
    public static void print_subseq(int i, int arr[], ArrayList<Integer> arrLi, int n) {
        if (i == n) {
            // System.out.println("hi"+i);
            System.out.println(arrLi);
            return;
        }
        // Important to remeber
        arrLi.add(arr[i]);  // add like trial room cloth
        print_subseq(i + 1, arr, arrLi, n);

        arrLi.remove(arrLi.size() - 1);  // then out the cloth 
        print_subseq(i + 1, arr, arrLi, n);
    }

    public static void main(String args[]) {
        int arr[] = { 3, 1, 2 };
        // System.out.println(Arrays.toString(arr));
        ArrayList<Integer> arrLi = new ArrayList<Integer>();

        // System.out.println(arrLi);
        print_subseq(0, arr, arrLi, arr.length);

    }

}
