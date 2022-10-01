package File1_Basics.Patterns;

import java.util.Scanner;

public class pat0 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i=1; i<=n ; i++){   // n number of rows
            
            System.out.print("*"); // work

            System.out.println(); // prepration of the next row
        }
    }
}
