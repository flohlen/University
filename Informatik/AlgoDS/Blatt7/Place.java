class Place {
    // Position des Platzes im Gitter (Zeile, Spalte)
    int row, col;

    // Nachbarn des Platzes: in Zeile 0 ist north = null, in Spalte 0 ist west = 0 etc.
    Place north, south, east, west;  

    Place(int row, int col, Place north, Place south, Place west, Place east) {
        this.row = row;
        this.col = col;
        this.north = north;
        this.south = south;
        this.west = west;
        this.east = east;
    }

    // getter/setter-Methoden (soweit erforderlich) muessen noch ergaenzt werden
    int getRow() {
        return this.row;
    }

    int getCol() {
        return this.col;
    }

    void setSouth(Place x){
        this.south = x;
    }

    void setEast(Place x){
        this.east = x;
    }

    Place getNorth(){
        return this.north;
    }

    Place getSouth(){
        return this.south;
    }

    Place getWest(){
        return this.west;
    }

    Place getEast(){
        return this.east;
    }
}
