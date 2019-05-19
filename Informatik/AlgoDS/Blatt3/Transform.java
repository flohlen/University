//import java.util.*;

class Transform{
	public static void main(String[] args){
        // Beispiel 1
        // String[] args = {"bargeld","mondschein","scheinscheinbar","geldschein","bar"};
        
        String[] cur_st, old_st = args;

        int counter = 0;

        while(counter < args.length) {

            cur_st = trans(old_st);

            for (int i = 0; i < cur_st.length; i ++) {
                if (cur_st[i].length() > 0) {
                    System.out.print(cur_st[i] + " ");
                }
            }
            System.out.print("\n");

            old_st = cur_st;
            counter++;
        }
    }

    public static String[] trans(String[] st) {

        StringBuilder[] st_sb = new StringBuilder[st.length];
        
        for (int i = 0; i < st.length; i++){
            st_sb[i] = new StringBuilder(st[i]);
        }

        for (int i = 0; i < st.length; i++) {
            for (int j = 0; j < st.length; j++) {
                
                if (i != j) {
                    
                    if (st[i].contains(st[j])){
                        
                        if (st_sb[i].length() < st_sb[j].length()) {
                            st_sb[j] = new StringBuilder(st[j].replace(st[i], ""));
                        } else {
                            st_sb[i] = new StringBuilder(st[i].replace(st[j], ""));
                        }

                        for (int k = 0; k < st.length; k++) {
                            st[k] = st_sb[k].toString();
                        }       
                        return st;
                    }
                }
            }
        }

        for (int k = 0; k < st.length; k++) {
            st[k] = st_sb[k].toString();
        }
        return st;
    }
}