import java.util.*;

class Findnumber {
  public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    Random i=new Random();
    int zufallszahl=i.nextInt(21);
    int versuche=0;
    while(true){
      System.out.print("Bitte geben sie eine Zahl zwischen 0 und 20 ein:");
      int zahl=sc.nextInt();
      if(zahl>20){
        System.out.print("\nDie von ihnen eingegebene Zahl war zu groﬂ");
      }
      else if(zahl<0){
        System.out.print("\nDie von ihnen eingegebene Zahl war zu klein");
      }
      else{
        versuche +=1;
        if(zahl==zufallszahl){
          System.out.print("\nRateversuch: "+zahl);
          System.out.print("\nErraten nach "+ versuche + " Runden");
          break;
        }
        else if(zahl<zufallszahl){
          System.out.print("\nRateversuch: "+zahl);
          System.out.print("\nZu klein");
        }
        else if(zahl>zufallszahl){
          System.out.print("\nRateversuch: "+zahl);
          System.out.print("\nZu gross");
        }
      }
    }

  }
}