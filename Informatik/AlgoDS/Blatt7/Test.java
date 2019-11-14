class Test {

    public static void main(String[] args) {
        SquareTown t = null;
        try {
            t = new SquareTown(Integer.parseInt(args[0]));
            System.out.println("Erzeugtes Gitter der Stadt: ");
            System.out.println(t);
        } catch (Exception e) {
            System.out.println("Aufruf: Test n");
            System.out.print(e);
        }
    }
    
}
