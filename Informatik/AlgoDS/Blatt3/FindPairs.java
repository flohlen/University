import java.util.*;


class FindPairs {
    public static void main(String[] args) {

        // Beispiel 1
        // String[] args = {"eis", "sie", "sei"};

        // Beispiel 2
        // String[] args = {"stil","eis","list","sie","Eis","Sie","ist","stil","still"};
        
        boolean batcat = true;

        for (int i = 0; i < args.length; i++) {
            for (int j = i+1; j < args.length; j++) {
                if (sortcat(args[i]).compareTo(sortcat(args[j])) == 0) {
                    System.out.println("Permutation gefunden: " + args[i] + " - " + args[j]);
                    batcat = true;
                }
            }
        }
        
        if (batcat) { System.out.println("Keine Permutation gefunden."); }
    }

    public static String sortcat(String cat) {
        char charcat[] = cat.toCharArray();
        Arrays.sort(charcat);
        return new String(charcat);
    }
}