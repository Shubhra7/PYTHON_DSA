import java.util.*;
import java.lang.*;
import java.io.*;

// When have to return ***only one sub sequence**** of sum that
// Striver video ==> 7

public class Sum_modified_subseq {
    public static boolean sum_seq(int ind,int arr[], ArrayList<Integer> bigL,int sum,int s){
        if(ind == arr.length){
            if(sum == s){
                System.err.println(bigL);
                return true;
            }
            else return false;
        }
        bigL.add(arr[ind]);
        s += arr[ind];
        if(sum_seq(ind+1, arr, bigL, sum, s) == true){
            return true;
        };              // Pick

        bigL.remove(bigL.size()-1);
        s -= arr[ind];

        if(sum_seq(ind+1, arr, bigL, sum, s) == true){
            return true;
        }  // Not pick

        return false;
    }
    public static void main(String[] args) {
        int arr[] = {1,2,1,1};
        int sum = 3;
        ArrayList<Integer> bigL = new ArrayList<Integer>();
        sum_seq(0,arr,bigL,sum,0);
    }
    
}
