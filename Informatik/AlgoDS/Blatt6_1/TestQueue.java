class TestQueue {

  public static void main(String[] args) {

    Queue<Integer> integerRing = new QueueRing<>();
    try {
      integerRing.enqueue(4);
    } catch (QueueException e) {
      e.printStackTrace();
    }

    boolean search = integerRing.search(10);
    System.out.println("10 wurde in integerRing " + (search ? "" : "nicht ") + "gefunden");
    search = integerRing.search(4);
    System.out.println("4 wurde in integerRing " + (search ? "" : "nicht ") + "gefunden");

    printLine();

    Queue<Person> studentRing = new QueueList<>();
    try {
      studentRing.enqueue(new Student("Astrid", "Ahorn"));
      studentRing.enqueue(new Student("Bertha", "Baer"));
      studentRing.enqueue(new Student("Dirk", "Dachs"));
      studentRing.enqueue(new Student("Egon", "Esel"));
      System.out.println("loesche: " + studentRing.dequeue());
      System.out.println("loesche: " + studentRing.dequeue());
      studentRing.enqueue(new Student("Fritz", "Flamingo"));
      studentRing.enqueue(new Student("Gabi", "Gazelle"));
      studentRing.enqueue(new Student("Hans", "Harmlos"));
      System.out.println("loesche: " + studentRing.dequeue());
      studentRing.enqueue(new Student("Susi", "Sorglos"));
    } catch (QueueException e) {
      System.out.println("Diese Ausschrift darf nicht erscheinen!");
    }
    System.out.println(studentRing);

    search = studentRing.search(new Student("Susi", "Sorglos"));
    System.out.println("Susi Sorglos wurde in studentRing " + (search ? "" : "nicht ") + "gefunden");
    search = studentRing.search(new Student("Astrid", "Ahorn"));
    System.out.println("Astrid Ahorn wurde in studentRing " + (search ? "" : "nicht ") + "gefunden");

    printLine();

    Queue<Person> professorList = new QueueList<>();
    try {
      professorList.enqueue(new Professor("Karla", "Nensa"));
      professorList.enqueue(new Professor("Klaus", "Ernst"));
      professorList.enqueue(new Professor("Cornelia", "Kilian"));
      professorList.enqueue(new Professor("Renate", "Manns"));
      System.out.println("loesche: " + professorList.dequeue());
      System.out.println("loesche: " + professorList.dequeue());
      professorList.enqueue(new Professor("Jannik", "Vellmer"));
      professorList.enqueue(new Professor("Sebastian", "Schauer"));
    } catch (QueueException e) {
      System.out.println("Diese Ausschrift darf nicht erscheinen!");
    }
    System.out.println(professorList);

    search = professorList.search(new Professor("Karla", "Nensa"));
    System.out.println("Karla Nensa wurde in professorList " + (search ? "" : "nicht ") + "gefunden");
    search = professorList.search(new Professor("Renate", "Manns"));
    System.out.println("Renate Manns wurde in professorList " + (search ? "" : "nicht ") + "gefunden");

    printLine();

    // System.out.println("Es gibt " + studentRing.count() + " Studenten, und " + professorList.count() + " Professoren");
    // PersonQueueComparator personQueueComparator = new PersonQueueComparator();
    // int compare = personQueueComparator.compare(studentRing, professorList);
    // if (compare == 0) {
    //   System.out.println("Professoren == Studenten");
    // } else if (compare < 0) {
    //   System.out.println("Professoren > Studenten");
    // } else if (compare > 0) {
    //   System.out.println("Professoren < Studenten");
    // }

    printLine();

    try {
      studentRing.merge(professorList);
    } catch (QueueException e) {
      e.printStackTrace();
    }

    System.out.println(studentRing);



//die folgenden Zeile duerfen nicht funktionieren
//    integerRing.merge(studentRing);
//    personQueueComparator.compare(studentRing, integerRing);

  }


  static void printLine() {
    System.out.println("\n-------------------------------------------------------------\n");
  }



}
