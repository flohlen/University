interface PersonQueue {

    void enqueue(Person who) throws QueueException;
    Person dequeue()  throws QueueException;

    int count();
    /*
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
    */

    void merge(Queue<T> other) throws QueueException;
    /*
    public void merge(Queue<T> other) throws QueueException {
        equeue(other.dequeue());
    }
    */
}
