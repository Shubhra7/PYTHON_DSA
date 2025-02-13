import java.util.ArrayList;
import java.util.Scanner;

public class array_input {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        
        while (sc.hasNext()) {
            if(sc.hasNextInt()){
                list.add(sc.nextInt());
            }else{
                String input=sc.next();
                if(input.equalsIgnoreCase("\n")){
                    break;
                }
            }
        }
        System.out.println("Your array is: "+list);
    }
    
}
