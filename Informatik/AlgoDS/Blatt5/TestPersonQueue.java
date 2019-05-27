class TestPersonQueue {

    public static void main(String[] args) {
        System.out.println("Zunaechst Test der Ringspeicher-Implementierung:");
        PersonQueue q = new PersonQueueRing();
        performTest(q);
        /* Fuer Test der Listen-Implementierung  die folgenden Zeilen einkommentieren: */
        System.out.println("Nun Test der Listen-Implementierung:");
        q = new PersonQueueList();
        performTest(q);
    }

    static void performTest(PersonQueue q) {
        try {
            q.enqueue(new Person("Astrid", "Ahorn"));
            q.enqueue(new Person("Bertha", "Baer"));
            q.enqueue(new Person("Dirk", "Dachs"));
            q.enqueue(new Person("Egon", "Esel"));
            System.out.println("loesche: " + q.dequeue());
            System.out.println("loesche: " + q.dequeue());
            q.enqueue(new Person("Fritz", "Flamingo"));
            q.enqueue(new Person("Gabi", "Gazelle"));
            q.enqueue(new Person("Hans", "Harmlos"));
            System.out.println("loesche: " + q.dequeue());
            q.enqueue(new Person("Susi", "Sorglos"));
        } catch (QueueException e) {
            System.out.println("Diese Ausschrift darf nicht erscheinen!");
        }
        try {
            q.enqueue(new Person("Paul", "Panther"));
        } catch (QueueException e) {
            System.out.println("Einfuegeversuch von Paul Panther fuehrt zu Ausnahme");
        }
        System.out.println(q);
        try {
            System.out.println("loesche: " + q.dequeue());
            System.out.println("loesche: " + q.dequeue());
            System.out.println("loesche: " + q.dequeue());
            System.out.println("loesche: " + q.dequeue());
            System.out.println("loesche: " + q.dequeue());
        } catch (QueueException e) {
            System.out.println("Einfuegeversuch von Paul Panther fuehrt zu Ausnahme");
        }
        try {
            System.out.println("loesche: " + q.dequeue());
        } catch (QueueException e) {
            System.out.println("Keiner mehr da");
        }
        try {
            System.out.println("loesche: " + q.dequeue());
        } catch (QueueException e) {
            System.out.println("Keiner mehr da");
        }
        System.out.println(q);
    }
    
}
