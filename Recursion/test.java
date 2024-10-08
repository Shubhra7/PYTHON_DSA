import java.util.Scanner;

public class test {

    public static boolean flag = false;  // For using like global variable

    public static void print_series(int n){
        if(n==2)
                flag= true;
        if(n==0){
            System.out.print(n+" ");
            return;
        }
        else
            System.out.print(n+" ");
            print_series(n-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the n value: ");
        int value = sc.nextInt();
        System.out.println(flag);
        print_series(value);
        sc.close();
        System.out.println(flag);

    }
    
}
