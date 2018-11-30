import time
import random

def init(x):
    return random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1)

# Berechnet eine Gewinnstrategie im Streichholzspiel
# mittels Backtracking.
# Falls für anziehenden Spieler
#      - keine Gewinnstrategie existiert, wird -1 zurueckgegeben (beliebiger Zug verliert)
#      - eine Gewinnstratie existiert, wird der Gewinnzug (1,2, oder 3) zurueckgegeben
def strategie(uebrig):
    if uebrig==1:
        return -1
    if 2<= uebrig and uebrig <=4:
        return uebrig-1
    else:
        for weniger in range(1,4):
            if strategie(uebrig-weniger)==-1:
                return weniger
        return -1


def strategie_memoization(uebrig,wb):
    if uebrig in wb:
        return wb[uebrig]
    if uebrig==1:
        wb[uebrig]=-1
        return -1
    if 2<= uebrig and uebrig <=4:
        wb[uebrig]=uebrig-1
        return uebrig-1
    else:
        for weniger in range(1,4):
            if strategie_memoization(uebrig-weniger,wb)==-1:
                wb[uebrig]=weniger
                return weniger
        return -1



def speedtest(streichhoelzer):
    print(" Ausgabe durch gewoehnliches Backtracking")

    t0 = time.process_time() 
    for j in range(1,streichhoelzer):
        print(strategie(j))
    t1 = time.process_time() - t0
    print("Benötigte Zeit ",t1,"Sekunden")

    print(" Ausgabe durch Backtracking mittels Memoization")

    t0 = time.process_time() 
    for j in range(1,streichhoelzer):
        print(strategie_memoization(j,{}))
    t1 = time.process_time() - t0
    print("Benötigte Zeit ",t1,"Sekunden")

#streichhoelzer=init(int(input("Geben Sie eine Anzahl von Streichhoelzern ein: ")))
streichhoelzer = [0,0,0,0,0,2,0]
#speedtest(streichhoelzer) #Vergleich mit und ohne Memoization 

#quit() # führt den interaktiven Teil nicht aus

spieler = 2 ##hier geben wir den anziehenden Spieler an, Computer ist Spieler 1.

while (streichhoelzer[0] > 0 or streichhoelzer[1] > 0 or streichhoelzer[2] > 0 or streichhoelzer[3] > 0 or streichhoelzer[4] > 0 or streichhoelzer[5] > 0 or streichhoelzer[6] > 0):

    print("")
    print("Es sind noch "+str(streichhoelzer)+" Streichhoelzer uebrig")
    print("")

    #falls keine Gewinnstrategie vorhanden ist, dann nehmen wir ein Streichholz vom ersten nicht leeren Haufen weg
    zug = (1,0 if (streichhoelzer[0]>0) else 1 if (streichhoelzer[1]>0) else 2 if (streichhoelzer[2]>0) else 3 if (streichhoelzer[3]>0) else 4 if (streichhoelzer[4]>0) else 5 if (streichhoelzer[5]>0) else 6)
    print(zug)

    if spieler == 1:
        if strategie(streichhoelzer) != -1:
            zug = strategie(streichhoelzer)

        print("Spieler 1 hat "+str(zug[0])+" Streichhoelz(er) von Haufen "+str(zug[1])+" weggenommen")
    else:
        zug = (int(input("Spieler "+str(spieler)+" ist an der Reihe, bitte Anzahl [min. 1, max. alle] eingeben: ")),int(input("Bitte Haufen [1-7] angeben: ")))

    if type(zug[0]) == str and zug[0].lower == "alle":
        zug[0] = streichhoelzer[zug[1]]

    if (streichhoelzer[int(zug[1])-1] - int(zug[0])) < 1 or not (zug[0] > 0 and zug[0] <= zug[0]):
        print("")
        print("!!!!!! Spieler " + str(spieler) + " hat verloren !!!!!!")
        break
    streichhoelzer[int(zug[1])-1] -= int(zug[0]) 
    spieler = 3-spieler
# while (streichhoelzer[0] >= 1 or streichhoelzer[1] >= 1 or streichhoelzer[2] >= 1 or streichhoelzer[3] >= 1 or streichhoelzer[4] >= 1 or streichhoelzer[5] >= 1 or streichhoelzer[6] >= 1):
#     print("")
#     print("Es sind noch "+str(streichhoelzer)+" Streichhoelzer uebrig")
#     print("")
#     zug=1
#     if spieler == 1:
#         if strategie(streichhoelzer)!=-1:
#             zug=strategie(streichhoelzer)
#         print("Spieler 1 hat "+str(zug)+" Streichhoelz(er) weggenommen")
#         ##falls keine Gewinnstrategie vorhanden ist, dann nehmen wir ein Streichholz weg
#     else:
#         zug = (int(input("Spieler "+str(spieler)+" ist an der Reihe, bitte Anzahl [min. 1, max. alle] eingeben: ")),int(input("Bitte Haufen [1-7] angeben: ")))
#     if streichhoelzer[int(zug[1])-1] - int(zug[0]) < 1 :
#         print("")
#         print("!!!!!! Spieler " + str(spieler) + " hat verloren !!!!!!")
#         break
#     print(int(zug[1])-1)
#     print(streichhoelzer[int(zug[1]-1)])
#     print(int(zug[0]))

#     streichhoelzer[int(zug[1]-1)]-=int(zug[0])
#     spieler = 3-spieler




# or not (zug==1 or zug==2 or zug==3)