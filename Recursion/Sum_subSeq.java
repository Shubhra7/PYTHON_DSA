import java.util.*;
import java.lang.*;
import java.io.*;

public class Sum_subSeq {
    public static void sum_seq(int ind,int arr[], ArrayList<Integer> bigL,int sum,int s){
        if(ind == arr.length){
            if(sum == s)
                System.err.println(bigL);
            return;
        }
        bigL.add(arr[ind]);
        s += arr[ind];
        sum_seq(ind+1, arr, bigL, sum, s);  // Pick

        bigL.remove(bigL.size()-1);
        s -= arr[ind];
        sum_seq(ind+1, arr, bigL, sum, s); // Not pick
    }
    public static void main(String[] args) {
        int arr[] = {1,2,1};
        int sum = 2;
        ArrayList<Integer> bigL = new ArrayList<Integer>();
        sum_seq(0,arr,bigL,sum,0);
    }
    
}
