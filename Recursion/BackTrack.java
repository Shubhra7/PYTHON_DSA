import java.util.Scanner;

public class BackTrack {
    public static void series_p(int i,int n){
        if(i>5) return;
        series_p(i+1,n);
        System.out.print(i+" + ");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of n: ");
        int n = sc.nextInt();
        series_p(0,n);
        sc.close();
    }
    
}
