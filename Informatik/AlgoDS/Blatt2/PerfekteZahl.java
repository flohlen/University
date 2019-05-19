import java.util.*;

class PerfekteZahl{
  public static void main(String[]args) {

    Scanner sc = new Scanner(System.in);
    
    System.out.print("Bitte geben sie an wieviele Perfekte Zahlen sie berechnet haben wollen\n");
    int menge = sc.nextInt();

    int j, summe;
    int i = 1;
    int zahl = 2;
        
    while (i <= menge) {
        j = 1;
        summe = 0;
      
        while (j < zahl) {
            if(zahl % j == 0) {
                summe += j;
            }
            j++;
        }

        if (summe == zahl) {
            System.out.print("Die "+ i + ". perfekte Zahl lautet: " + zahl + "\n");
            i++;
        }
        zahl++; 
    }

  }
}