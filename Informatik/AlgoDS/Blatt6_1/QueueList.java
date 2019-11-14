class QueueList<T> implements Queue<T> {

    // Aushaengen bei head, Einhaengen bei tail
    private Node head = null;
    private Node tail = null;
	private T data;

    // kein Ueberlauf moeglich -> kein throws
    public void enqueue(T data) {
        System.out.println("enqueue aufgerufen fuer: " + data);
        Node newNode = new Node(data, null);
        if (head == null) {
            head = newNode;
        } else {
            tail.setNext(newNode);
        }
        tail = newNode;
    }

    public T dequeue()  throws QueueException {
        if (head == null) {
            throw new QueueException();
        } else {
            T result = (T) head.getT();
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
        return i;
    }

    public void merge(Queue<T> other) throws QueueException {
        enqueue(other.dequeue());
    }

    public String toString() {
        StringBuilder result = new StringBuilder("Inhalt Liste: \n");
        for (Node p = head;  p != null; p = p.getNext()) {
            result.append("    " + p.getT().toString() + "\n");
        }
        return new String(result);
    }

    boolean search(T data) {
        for (Node p = head;  p != null; p = p.getNext()) {
            if(p.getT().toString()==data.toString()){
                return true;
            }
            else{
                return false;
            }
        }
        return false;
    }
}
