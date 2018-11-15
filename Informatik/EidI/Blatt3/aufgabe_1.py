def lies_zeile(x):
    anzahl_k = 0
    tupel = ()
    for char in x:
        if char == ",":
            anzahl_k += 1
    if anzahl_k == 2:
        tupel = x.split(",")
        return tupel
    else:
        return -1

def lies_datei(x):
    
    l_datei = open(x+".csv","r")

    tupel_liste = []

    for x in l_datei:
        tupel_liste.append(lies_zeile(x))

    l_datei.close()

    return tupel_liste

def hat_schauspieler(x,zk):

    for i in x:
        if zk in i:
            return True
    return False

def schauspieler_zusammenarbeit(x,zk):

    schauspieler_liste = []

    for i in x:
        if zk in i:
            schauspieler_liste.append(i[1])

    return schauspieler_liste

def füge_ein(x,t):

    master_liste = []

    for i, z in x:
        if ord(i[-1][0]) < ord(t[-1][0]):
            master_liste.insert(t,z)
    
    return master_liste

print(schauspieler_zusammenarbeit(lies_datei("hollywood"),"The Fugitive"))

print(hat_schauspieler(lies_datei("hollywood"),"Sam Neill"))