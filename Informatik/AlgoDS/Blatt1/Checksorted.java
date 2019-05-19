import java.util.*;

class CheckSorted{
  public static void main(String[]args){
    int[] a = {2, 4, 5, 6, 9, 12, 17};
    boolean f = true;
    int j = a.length();
    j=j-2;
    for(int i=1; i<=j; i++){
      int tmp=a[i-1];
      if(tmp>a[i]){
        System.out.print("Das Array ist nicht sortiert");
        f=false;
        break;
      }
    }
    if(f){
      System.out.print("Das Array ist sortiert");
    }
  }
}