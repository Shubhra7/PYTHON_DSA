// Search an element in a matrix in Java
// Here, in this page we will discuss the program to print the spiral traversal 
// of the matrix in Java programming language. We’re given a n x n matrix and the 
// value of the element in the matrix that needs to be found.
// If the searched element is present in the matrix, we must find its position.
// Otherwise, “Not Found” must be printed.
// Every row and column in the specified matrix is sorted in ascending order.

// *** matrix must be sorted row wise *****

// link: https://prepinsta.com/java-program/search-an-element-in-a-matrix/

import java.util.*;
import java.io.*;

class search_in_matrix {
    public static void main(String[] args) {
        // System.out.println("hi");
        int a[][] = { { 0, 1, 2, 3 }, { 4, 5, 6, 7 }, { 8, 9, 10, 11 } };
        int row = a.length;
        int col = a[0].length;
        int i, j, search = 11, flag = 1;
        i = 0;
        j = col - 1;
        while (i < row && j >= 0) {
            // System.out.println("values: " + i + " - " + j);
            if (a[i][j] == search) {
                System.out.println("place: " + i + " " + j);
                flag = 0;
                break;
            } else if (search > a[i][j]) {
                i++;
            } else {
                j--;
            }
        }
        if (flag == 1) {
            System.out.println("Not found!!");
        }
    }
}