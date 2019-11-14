interface Queue<T> {

    void enqueue(T data) throws QueueException;
    T dequeue()  throws QueueException;

    int count();
    void merge(Queue<T> other) throws QueueException;
    
}
