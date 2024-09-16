import java.util.*;
import java.io.*;

public class Sieve_of_Erathosthenes{
    static boolean isPrime(int n){
        if(n<=1){
            return false;
        }
        if(n<=3){
            return true;
        }
        if(n%2==0 || n%3==0){
            return false;
        }
        int i=5;
        while (i*i <= n) {
            if(n%i==0 || n%(i+2)==0){
                return false;
            }
        i += 6;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("HI bubai");
        System.out.println("16: "+isPrime(16));
        System.out.println("17: "+isPrime(17));
        System.out.println("17: "+isPrime(19));
    }
}