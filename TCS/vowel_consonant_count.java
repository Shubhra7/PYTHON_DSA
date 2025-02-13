import java.util.Scanner;

public class vowel_consonant_count {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int v=0,c=0;
        String input = sc.nextLine().toLowerCase();
        for(char ch: input.toCharArray()){
            if(Character.isLetter(ch)){
                if("aeiou".indexOf(ch) != -1){
                    v++;
                }else{
                    c++;
                }
            }
        }
        System.out.println(v+" "+c);
        sc.close();
    }
}
