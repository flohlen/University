class PersonQueueComparator<T/* extends Person<T> & Student<T> & Professor<T> */> {

    public int compare(T o1, T o2) {
        
        int o1_c = count(o1);
        int o2_c = count(o2);

        if (o1_c < o2_c) {return -1;}
        else if (o1_c == o2_c) {return 0;}
        else {return 1;}
    }
}
