package File1_Basics.Patterns;

// 5
//     *
//    **
//   ***
//  ****
// *****

import java.util.Scanner;

public class pat4 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=1 ; i<=n ; i++){

            // print space
            for(int j=1 ; j<=n-i ; j++){
                System.out.print(" ");
            }

            // print *
            for(int k=1; k<=i ; k++){
                System.out.print("*");
            }

            // Prepration for the next line, i++ is also the prepration for next line
            System.out.println();
        }
    }
}
