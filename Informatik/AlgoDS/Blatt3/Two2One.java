//import java.util.*;

/*class Two2One{

    public static void main(String[]args){

        Scanner sc = new Scanner(System.in);

        System.out.print("Bitte Länge von a eingeben: ");
        int a_n = sc.nextInt();

        int a[] = new int[a_n];

        System.out.print("Bitte die Elemente von a durch Leerzeichen getrennt eingeben: ");
        for (int i = 0; i < a_n; i++){
            a[i] = sc.nextInt();  
        }

        System.out.print("Bitte Länge von b eingeben: ");
        int b_n = sc.nextInt();

        int b[] = new int[b_n];

        System.out.print("Bitte die Elemente von b durch Leerzeichen getrennt eingeben: ");
        for (int i = 0; i < b_n; i++){
            b[i] = sc.nextInt();
        }

        System.out.print("Bitte n eingeben: ");
        int n = sc.nextInt();
        
        // Beispiel 1
        // int a[] = {1,2,3};
        // int b[] = {1,2,3,4,5};
        // int n = 5;

        two2one(a, b, n);

    }

    public static void two2one(int[] a, int[] b, int n) {

        int[][] e_a = new int[n][];

        for (int i = 0; i < n; i++){
            e_a[i] = (i%2 == 0) ? a : b; 
        }

        for (int i = 0; i < e_a.length; i++){
            for (int j = 0; j < e_a[i].length; j++){
                System.out.print(e_a[i][j] + " ");
            }
            System.out.print("\n");
        }
    }

}*/