import time
import random

def init(x):
    return random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1),random.randint(1,x+1)

streichhoelzer=init(int(input("Maximalwert: ")))

print("")
print("Spielstand: " + str(streichhoelzer))
print("")


# Berechnet eine Gewinnstrategie im Streichholzspiel
# mittels Backtracking.
# Falls für anziehenden Spieler
#      - keine Gewinnstrategie existiert, wird -1 zurueckgegeben (beliebiger Zug verliert)
#      - eine Gewinnstratie existiert, wird der Gewinnzug (1,2, oder 3) zurueckgegeben

def strategie_memoization(uebrig,wb):

    if uebrig in wb:
        return wb[uebrig]

    # nicht leere haufen
    nl_haufen = 0

    for i in uebrig:
        if uebrig[i] > 0
            nl_haufen += 1

    if (nl_haufen % 2 == 1):
        e_haufen = 0
        n_haufen = 0
        for i in uebrig:
            if uebrig[i] == 1:
                e_haufen += 1
            elif uebrig[i] == 0:
                n_haufen += 1

        if (e_haufen+n_haufen == 7):
            if e_haufen % 2 == 1:
                

            if uebrig[i] != 1 and uebrig[i] != 0:
                uebrig[i] -= (uebrig[i]-1)
                break
            



                if uebrig[i] > (uebrig[i]-2):
                    uebrig[i] -= (uebrig[i]-2)
                    break
                else:
                    uebrig[i] -= uebrig[i]
                    break    
            elif uebrig[i] != 0:
                uebrig[i] -= uebrig[i]
                break
    else:
        for i in uebrig:
            if uebrig[i] > 1:
                uebrig[i] -= (uebrig[i])
                break
            #else:
             #   uebrig[i] -= (uebrig[i]-2)
              #  break

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
    print(" Ausgabe durch Backtracking mittels Memoization ")

    t0 = time.process_time()
    for i in range(0,6):
        for j in range(1,streichhoelzer[i]):
            print(strategie_memoization((i,j),{}))
    t1 = time.process_time() - t0
    print("Benötigte Zeit ",t1,"Sekunden")

speedtest(streichhoelzer) #Vergleich mit und ohne Memoization 
