import java.lang.StringBuilder;
class SquareTown {

    Place upperLeft = null;
    Place bottomRight = null;
     
    SquareTown(int n) {
        upperLeft = new Place(0, 0, null, null, null, null);
        // initial ist prevLine die oberste Zeile
        Place[] prevLine = new Place[n];
        prevLine[0] = upperLeft;
        for (int col = 1; col < n; ++col) {
            prevLine[col] = new Place(0, col, null, null, prevLine[col - 1], null);
        }
        for (int row = 1; row < n; ++row) {
            Place[] nextLine = new Place[n];
            nextLine[0] = new Place(row, 0, prevLine[0], null, null, null);
            for (int col = 1; col < n; ++col) {
                nextLine[col] = new Place(row, col, prevLine[col], null, nextLine[col - 1], null);
            }
            prevLine = nextLine;
        }
        bottomRight = prevLine[n-1];
        addSouthAndEast();
    }

    void addSouthAndEast() {
        Place temp = bottomRight;
        Place temp_1 = bottomRight;

        for (int i = bottomRight.getCol(); i >= 0; --i) {
            for (int j = bottomRight.getRow(); j >= 0; --j) {
                try {
                    Place tempo = temp.getWest();
                    tempo.setEast(temp);
                    temp = tempo;
                } catch (Exception e) { continue; }
            }
            temp_1 = temp_1.getNorth();
            temp = temp_1;
        }

        temp = bottomRight;
        temp_1 = bottomRight;
        
        for (int i = bottomRight.getCol(); i >= 0; i--) {
            for (int j = bottomRight.getRow(); j >= 0; j--) {
                try {
                    Place tempo = temp.getNorth();
                    tempo.setSouth(temp);
                    temp = tempo;
                } catch (Exception e) { continue; }
            }
            temp_1 = temp_1.getWest();
            temp = temp_1;
        }
    }

    public String toString() {
        
        StringBuilder retString = new StringBuilder();

        Place temp = upperLeft;

        Place temp_1 = upperLeft;
        Place temp_2 = upperLeft;

        for (int i = 0; i <= bottomRight.getRow(); i++) {
            for (int j = 0; j <= bottomRight.getCol(); j++) {

                retString.append("(" + temp.getRow() + ", " + temp.getCol() + ") ");
                if(temp.getNorth() != null) {
                    Place tempo = temp.getNorth();
                    retString.append("n = (" + tempo.getRow() + ", " + tempo.getCol() + ") ");
                }
                if(temp.getSouth() != null) {
                    Place tempo = temp.getSouth();
                    retString.append("s = (" + tempo.getRow() + ", " + tempo.getCol() + ") ");
                }
                if(temp.getWest() != null) {
                    Place tempo = temp.getWest();
                    retString.append("w = (" + tempo.getRow() + ", " + tempo.getCol() + ") ");
                }
                if(temp.getEast() != null) {
                    Place tempo = temp.getEast();
                    retString.append("e = (" + tempo.getRow() + ", " + tempo.getCol() + ") ");
                }
                retString.append("\n");


                temp_1 = temp_1.getEast();
                temp = temp_1;
            }

            temp_2 = temp_2.getSouth();
            temp = temp_2;
            temp_1 = temp_2;
        }

        return retString.toString();
    }
}