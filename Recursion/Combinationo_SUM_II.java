// Link: https://leetcode.com/problems/combination-sum-ii/
// Video link: https://www.youtube.com/watch?v=G1fRTGRxXU8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=11

import java.util.ArrayList;
import java.util.Arrays;

public class Combinationo_SUM_II {
    static void findCombi(int index, int arr[], ArrayList<Integer> ds, int target){
        if(target == 0){
            System.out.println(ds);
            return;
        }
        for(int i=index; i<arr.length ;i++){
            if(i>index && arr[i]==arr[i-1]) continue; // i>index for checking first time or not, if first time then allow
            if(target < arr[i]) break;  // if target is less then not to do rest branch 

            ds.add(arr[i]);
            findCombi(i+1, arr, ds, target-arr[i]); 
            ds.remove(ds.size()-1); // because after left hand the elemnt should out to remove
        }
    }

    public static void main(String[] args) {
        int arr[] ={10,1,2,7,6,1,5};
        Arrays.sort(arr);  // for lesological 
        ArrayList<Integer> ds = new ArrayList<>();
        int target=8;

        findCombi(0,arr,ds,target);

    }
}