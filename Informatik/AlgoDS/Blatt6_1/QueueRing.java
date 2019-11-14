class QueueRing<T> implements Queue<T> {

    static final int SIZE = 10;

    private int number = 0;
    private int in = 0;
    private int out = 0;
    private T[] elements = (T[]) new Object[SIZE];
	private T data;

    public void enqueue(T data) throws QueueException {
        System.out.println("enqueue aufgerufen fuer: " + data);
        if (number == SIZE) {
            throw new QueueException();
        } else {
            elements[in] = data;
            ++number;
            in = (in + 1) % SIZE;
        }
    }

    public T dequeue()  throws QueueException {
        if (number == 0) {
            throw new QueueException();
        } else {
            --number;
            T result = elements[out];
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
        enqueue(other.dequeue());
    }

    public String toString() {
        StringBuilder result = new StringBuilder("Inhalt Ringspeicher: \n");
        for (int i = 0, where = out; i < number; ++i, where = (where + 1) % SIZE) {
            result.append("    " + elements[where].toString() + "\n");
        }
        return new String(result);
    }

    boolean search(T data) {
        for (int i = 0, where = out; i < number; ++i, where = (where + 1) % SIZE) {
            if(elements[where].toString()==data) {
                return true;
            }
            else{
                return false;
            }
        }
        return false;
    }
}
