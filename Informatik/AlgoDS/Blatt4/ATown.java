class ATown {

    public static void main(String[] args) {
        Club soccer = new Club("Fussballverein");
        Club carnival = new Club("Karnelvalsverein");
        // erstes true = jaehrliche Grußnachrichten, zweites true = erst ab 18
        Club singers = new Club("Gesangsverein", true, true);  
        Club[] clubs = new Club[3];
        clubs[0] = soccer;
        clubs[1] = carnival;
        clubs[2] = singers;

        Person[] persons = new Person[GeneralInfo.MAX_NUMBER_OF_PERSONS];
        persons[0] = new Woman("Karin", 33);
        persons[1]  = new Woman("Susi", 44);
        persons[2] = new Woman("Petra", 7);
        persons[3] = new Man("Dieter");
        persons[4] = new Man("Moritz", 14); // darf also ab dem 4. Jahr in Gesangsverein
        persons[5] = new Man("Paul", 22);
        persons[6] = new Man("Egon", 58);
        persons[7] = new Man("Jan", 26);
        persons[8] = new Woman("Hanna", 14);
        persons[9] = new Woman("Sabine");
        for (Person person: persons) {
            person.sendInfo(clubs);
        }
        for (int i = 0; i < GeneralInfo.NUMBER_YEARS; ++i) {
            for (Person person: persons) {
                person.simulateNextYear();
            }
            for (Club club: clubs) {
                club.simulateNextYear();
            }
            System.out.println("\n---------\n");
            System.out.println((i+1) + "-tes Jahr:");
            for (Club club: clubs) {
                club.showAllInfo();
            }
        }

        System.out.println();
        System.out.println(persons[0] + " hat folgende Nachrichten des Gesangsvereins erhalten:");
        persons[0].showYearlyMessages();

        // Die folgende Ausschrift soll auch dann korrekt
        // funktionieren, wenn das Array persons verändert und der
        // Rest des Programms beibehalten wird. Wird beispielsweise im
        // Array die Frau Petra durch den Mann Peter ersetzt, so muss
        // ein Mann mehr und eine Frau weniger angezeigt werden.
        System.out.println("Das Programm hat " +  Person.getNumberOfMen()
                           + " Maenner und " + Person.getNumberOfWomen() + " Frauen beruecksichtigt.");
    }
    
}
