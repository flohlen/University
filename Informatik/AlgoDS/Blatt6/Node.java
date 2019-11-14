class Node {

    private Node next;
    private Person person;

    Node(Person person, Node next) {
        this.next = next;
        this.person = person;
    }

    Person getPerson() {
        return person;
    }

    void setNext(Node next) {
        this.next = next;
    }

    Node getNext() {
        return next;
    }
    
}
