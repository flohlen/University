class PersonQueueList implements PersonQueue {

    // Aushaengen bei head, Einhaengen bei tail
    private Node head = null;
    private Node tail = null;

    // kein Ueberlauf moeglich -> kein throws
    public void enqueue(Person who) {
        System.out.println("enqueue aufgerufen fuer: " + who);
        Node newNode = new Node(who, null);
        if (head == null) {
            head = newNode;
        } else {
            tail.setNext(newNode);
        }
        tail = newNode;
    }

    public Person dequeue()  throws QueueException {
        if (head == null) {
            throw new QueueException();
        } else {
            Person result = head.getPerson();
            head = head.getNext();
            if (head == null) {  // Liste ist jetzt leer
                tail = null;
            }
            return result;
        }
    }

    public int count() {
        int i = 0;
        while(true) {
            try {
                enqueue(dequeue());
                i+=1;
            } finally {
                break;
            }
        }
        // return anzahl an aktuell gespeicherten Einträge
        return i;
    }

    public void merge(Queue<T> other) throws QueueException {
        equeue(other.dequeue());
    }

    public String toString() {
        StringBuilder result = new StringBuilder("Inhalt Liste: \n");
        for (Node p = head;  p != null; p = p.getNext()) {
            result.append("    " + p.getPerson().toString() + "\n");
        }
        return new String(result);
    }
    
}
