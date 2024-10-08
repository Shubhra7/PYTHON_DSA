import java.util.*;
import java.io.*;


class One_to_N_print {

    public static void series_print(int i, int n){
        if(i>n){
            return;
        }
        System.out.print(i+" + ");
        series_print(i+1, n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of n: ");
        int n = sc.nextInt();
        sc.close();
        series_print(0,n);
    

    }
}