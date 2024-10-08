// Have to make the combination which is the target sum
// one element can used multiple times

import java.util.ArrayList;

public class Combination_sum_L8 {
    static void findCombination(int index,int arr[],ArrayList<Integer> ds,int target){
        if(index == arr.length-1){
            if(target==0){
                System.out.println(ds);
            }
            return;
        }
        if(target>=arr[index]){
        ds.add(arr[index]);
        findCombination(index,arr,ds, target-arr[index]);

        ds.remove(ds.size()-1);
    }
        findCombination(index+1,arr,ds,target);
    }
    public static void main(String[] args) {
        int arr[] ={2,3,6,7};
        int target=7;
        ArrayList<Integer> ds = new ArrayList<>();
        findCombination(0,arr,ds,target);
    }
    
}
