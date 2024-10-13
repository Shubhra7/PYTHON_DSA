import java.util.ArrayList;

public class Subset_Sum_1 {
    static void findCombiSum(int index, int arr[],ArrayList<Integer> ds,int sum){
        if(index == arr.length){
            ds.add(sum);
            
            return;
        }

        // pick the element
        sum += arr[index];
        findCombiSum(index + 1, arr, ds, sum);

        // do-not pick the element
        sum -= arr[index];
        findCombiSum(index + 1, arr, ds, sum);
    }

    public static void main(String[] args) {
        // int arr[] = {3,1,2};
        int arr[] = { 1,2,-3 };
        // int arr[] = {-3,-2,-1,0,0,1,2,3};
        ArrayList<Integer> sumArr = new ArrayList<>();
        findCombiSum(0,arr,sumArr,0);
        System.out.println(sumArr);
    }
}