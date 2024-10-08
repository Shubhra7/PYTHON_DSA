import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class test {
    public static ArrayList<Integer> b=new ArrayList<>();

    public static void merge(int arr[],int low, int mid, int high){
        int l1=low,l2=mid+1,i;
        
        while(l1<=mid && l2<=high){
            if(arr[l1]<=arr[l2]){
                b.add(arr[l1]);
                l1++;
            }else{
                b.add(arr[l2]);
                l2++;
            }
            while (l1<=mid) {
                b.add(arr[l1++]);
            }
            while (l2<=high) {
                b.add(arr[l2++]);
            }
            for(i=low;i<=high;i++){
                arr[i]=b.get(i-low);
            }
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
