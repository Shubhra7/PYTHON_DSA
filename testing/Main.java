// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.io.*;
import java.util.*;

class A{
    int value=0;
    A(int value){
        this.value=value;
    }
    void printvalue(){
        System.out.println("The value is: "+value);
    }
}

class B extends A{
    int value1;
    B(int value1){
        this.value1=value1;
    }
    void justprint(){
        System.out.println("The value1 is: "+value1);
    }
}

class Main {
    public static void main(String[] args) {
        A obj=new A(4);
        obj.printvalue();
        
    }
}