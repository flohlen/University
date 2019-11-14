class PersonQueueRing implements PersonQueue {

    static final int SIZE = 5;

    private int number = 0;
    private int in = 0;
    private int out = 0;
    private Person[] elements = new Person[SIZE];

    public void enqueue(Person who) throws QueueException {
        System.out.println("enqueue aufgerufen fuer: " + who);
        if (number == SIZE) {
            throw new QueueException();
        } else {
            elements[in] = who;
            ++number;
            in = (in + 1) % SIZE;
        }
    }

    public Person dequeue()  throws QueueException {
        if (number == 0) {
            throw new QueueException();
        } else {
            --number;
            Person result = elements[out];
            out = (out + 1) %SIZE;
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
        StringBuilder result = new StringBuilder("Inhalt Ringspeicher: \n");
        for (int i = 0, where = out; i < number; ++i, where = (where + 1) % SIZE) {
            result.append("    " + elements[where].toString() + "\n");
        }
        return new String(result);
    }
    
}
