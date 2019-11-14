class Person {

    private String firstname;
    private String surname;

    Person(String firstname, String surname) {
        this.firstname = firstname;
        this.surname = surname;
    }

    public String toString() {
        return firstname + " " + surname;
    }
    
}
