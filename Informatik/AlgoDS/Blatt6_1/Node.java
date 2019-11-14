class Node<T> {

    private Node next;
    private T t;

    Node(T t, Node next) {
        this.next = next;
        this.t = t;
    }

    T getT() {
        return t;
    }

    void setNext(Node next) {
        this.next = next;
    }

    Node getNext() {
        return next;
    }
    
}
