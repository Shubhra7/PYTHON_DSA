import java.util.Scanner;

class Sum_of_digit_in_string{
    public static void main(String argsString[]){
        Scanner sc = new Scanner(System.in);
        int sum=0;
        String input = sc.nextLine();
        for(char ch: input.toCharArray()){
            if(Character.isDigit(ch)){
                sum += Character.getNumericValue(ch);
            }
        }
        System.out.println("THe sum is: "+sum);
        sc.close();
    }
}