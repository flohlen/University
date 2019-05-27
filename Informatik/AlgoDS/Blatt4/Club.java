public class Club{

    static Club[] clubs;
    String name;
    boolean grussnachricht, ab18;
    Person[] mitglieder = new Person[GeneralInfo.MAX_NUMBER_OF_PERSONS];

    public Club(String name) {
        this.name = name;
        this.grussnachricht = false;
        this.ab18 = false;

        clubs[clubs.length + 1] = this;
    }

    public Club(String name, boolean grussnachricht, boolean ab18) {
        this.name = name;
        this.grussnachricht = grussnachricht;
        this.ab18 = ab18;

        clubs[clubs.length + 1] = this;
    }

    public void beitreten(Person person) {
        if (person.alter >= 18 && this.ab18) {
            this.mitglieder[this.mitglieder.length + 1] = person;
        }
    }

    public void verlassen(Person person) {
        for (int i = 0; i < this.mitglieder.length; i++) {
            if (this.mitglieder[i].equals(person)) {
                p_remove(this.mitglieder, this.mitglieder[i]);
                break;
            }
        }
    }
    
    public void simulateNextYear() {
        GeneralInfo.YEAR++;
        for(Club club : clubs) {
            if (club.grussnachricht) {
                for(Person person : club.mitglieder) {
                    person.gruesse("Gruesse im Jahr " + GeneralInfo.YEAR + " von Verein " + club);
                }
            }
        }
    }

    public void showAllInfo() {
        System.out.print(this.name + " mit Mitgliedern: ");
        for(int i = 0; i < this.mitglieder.length; i++) {
            System.out.print(this.mitglieder[i] + " ");
        }
        System.out.print("\n");
    }

    Person[] p_remove(Person[] a, Person b) {
        Person[] temp = new Person[a.length-1];
        int p = 0;

        for(int i = 0; i < a.length; i++) {
            if(!a[i].equals(b)){
                temp[p] = a[i];
                p++;
            }
        }

        return temp;
    }

}