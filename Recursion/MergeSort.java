import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class MergeSort {
    public static void merge(int arr[],int left,int mid, int right){
        int i=left;
        int j=mid+1;
        ArrayList<Integer> temp = new ArrayList<>();
        while( i<= mid && j<= right){
            if(arr[i] <= arr[j]){
                temp.add(arr[i]);
                i++;
            }else{
                temp.add(arr[j]);
                j++;
            }
        }
        while(i<=mid){
            temp.add(arr[i]);
            i++;
        }
        while(j<=right){
            temp.add(arr[j]);
            j++;
        }

        for(int k=left;k<=right;k++){
            arr[k]=temp.get(k-left);
        }
    }

    public static void mergeS(int arr[],int left, int right){
        if(left >= right) return;
        int mid = left + (right-left)/2;
        mergeS(arr, left, mid);
        mergeS(arr, mid+1, right);
        merge(arr,left,mid,right);
    }
    public static void main(String args[]){
        // int []arr = {3,1,5,2,0,9};
        int []arr = {9,4,5,6,3,1,1};

        mergeS(arr,0,arr.length-1);

        System.out.println(Arrays.toString(arr));
    }
    
}
