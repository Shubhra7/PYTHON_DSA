import java.util.*;

public class Quick_sort {

    static int partition(int arr[], int low, int high) {
        int i = low + 1;
        int j = high;
        int pvloc = arr[low];
        while (i <= j) {
            while (arr[i] < pvloc && i <high) {   // i<high is important line
                i++;
            }
            while (arr[j] > pvloc)
                j--;
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            } else
                i++;
        }
        arr[low] = arr[j];
        arr[j] = pvloc;
        return j;
    }

    static void quickS(int arr[], int low, int high) {
        if (low >= high)
            return;
        int pivot = partition(arr, low, high);
        quickS(arr, low, pivot - 1);
        quickS(arr, pivot + 1, high);
    }

    public static void main(String[] args) {
        int[] arr = { 2, 3, 1, 5, 21, 7 };
        quickS(arr, 0, arr.length - 1);
        System.out.println("After sorting answer is: ");
        System.out.println(Arrays.toString(arr));
    }
}
