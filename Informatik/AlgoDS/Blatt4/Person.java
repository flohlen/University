import java.util.*;

class Person {

    Random zz = new Random();

    static int amountMen = 0;
    static int amountWomen = 0;
    
    Club[] clubs;

    String name;
    Club[] vereine;
    String[] nachrichten;
    int alter;
    boolean volljaehrig = true;

    public void sendInfo(Club[] clubus) {
        this.clubs = clubus;   
    }

    public static int  getNumberOfMen() {
        return amountMen;
    }

    public static int getNumberOfWomen() {
        return amountWomen;
    }

    void simulateNextYear() {
            
        this.alter++;
        if(this.alter >= 18 && !this.volljaehrig) {
            this.volljaehrig = true;
        }

        for (int j = 0; j < clubs.length; j++) {
            for (int i = 0; i < this.vereine.length; i++) {
                if (this.vereine[i].equals(clubs[j])) {
                    int zzz = zz.nextInt(2);
                    if (zzz == 0) {
                        clubs[j].verlassen(this);
                        c_remove(this.vereine, this.vereine[i]);
                    }
                } else {
                    int zzz = zz.nextInt(2);
                    if (zzz == 0) {
                        clubs[j].beitreten(this);
                        this.vereine[i+1] = clubs[j];
                    }
                }
            }
        }
    }

    public void showYearlyMessages() {
        for (String nachricht : this.nachrichten) {
            System.out.print(nachricht + "\n");
        }
    }

    Club[] c_remove(Club[] a, Club b) {
        Club[] temp = new Club[a.length-1];
        int p = 0;

        for(int i = 0; i < a.length; i++) {
            if(!a[i].equals(b)){
                temp[p] = a[i];
                p++;
            }
        }

        return temp;
    } 

    public void gruesse(String message) {
        this.nachrichten[this.nachrichten.length + 1] = message;
    }

    public void firstSelection() {

        for (Club club : clubs) {
            int zzz = zz.nextInt(2);
            if (zzz == 0) {
                club.beitreten(this);
            }
        }

    }
}

class Man extends Person { 

    public Man(String name) {
        super.name = name;
        super.amountMen++;
        super.firstSelection();
    }

    public Man(String name, int alter) {
        if (alter < 18) super.volljaehrig = false;
        
        super.name = name;
        super.alter = alter;
        super.amountMen++;
        super.firstSelection();
    }
}


class Woman extends Person{
    public Woman (String name, int alter) {
        if (alter < 18) super.volljaehrig = false;

        super.alter = alter;
        super.name = name;
        super.amountWomen++;
        super.firstSelection();
    }
    
    public Woman (String name) {
        super.name = name;
        super.amountWomen++;
        super.firstSelection();

        // for (Club club : clubs) {
        //     int zzz = zz.nextInt(2);
        //     if (zzz == 0) {
        //         club.beitreten(this);
        //     }
        // }
    }
}
