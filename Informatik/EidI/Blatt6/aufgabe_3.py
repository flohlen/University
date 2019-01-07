import sys
import time

# Sie duerfen diese Funktion nicht veraendern.
def sortiere(kleiner,L):
    trenner = 0
    while trenner != len(L):
        for i in range(trenner,len(L)):
            if kleiner(L[i],L[trenner]):
                L[trenner], L[i] = L[i], L[trenner]
        trenner += 1
    return L


# Sie duerfen diese Funktion nicht veraendern.
def ausgabe(stand):
	for i in range(9):
		tmp=""
		if i==3 or i==6:
			print("-"*30)
		for j in range(9):
			if j==3 or j==6: 
				tmp+="   |  "
			d=stand[(i,j)]
			if len(d)==1:
				for e in d:
					tmp+=" "+str(e)
			else: 
				tmp+=" "+"*"
		print(tmp)


# Sie duerfen diese Funktion nicht veraendern.
def kopie(stand):
	return {(i,j):stand[(i,j)].copy() for i in range(9) for j in range(9)}


# Sie duerfen diese Funktion nicht veraendern.
def buersten(sudoku):
	def abhaengig(i,j,x,y):
		return (not((i==x) and (j==y))) and ((i==x) or (j==y) or (i//3==x//3) and (j//3==y//3))
	sudokuk=kopie(sudoku)
	entfernt=False
	effects=[(wert,x,y) for i in range(9) for j in range(9) for x in range(9) for y in range(9) \
            for wert in sudokuk[(i,j)] if len(sudokuk[(i,j)])==1 and wert in sudokuk[(x,y)] and abhaengig(i,j,x,y)]

	for (wert,x,y) in effects:
                if wert in sudokuk[(x,y)]: 
                    sudokuk[(x,y)].remove(wert)
                    entfernt=True
	if entfernt: 
            sudokuk=buersten(sudokuk)
	return sudokuk

# Sie duerfen diese Funktion nicht veraendern.
def erfuellbar(stand):
	if len([stand[(i,j)] for i in range(9) for j in range(9) if len(stand[(i,j)])==0])>=1: 
		return False
	elif len([stand[(i,j)] for i in range(9) for j in range(9) if len(stand[(i,j)])==1])==81: 
		print("Wir haben eine Loesung gefunden")
		ausgabe(stand)
		return True
	else:
                nonsingletons=[(i,j,stand[(i,j)]) for i in range(9) for j in range(9) if len(stand[(i,j)])>1]
                cmp = lambda a,b: len(a[2])>len(b[2])
                nonsingletons = sortiere(cmp,nonsingletons)
                (i,j,ziffern)=nonsingletons.pop()
                ziffernkopie=ziffern.copy()
                old=stand.copy()
                for x in ziffernkopie:
                        stand[(i,j)].clear()
                        stand[(i,j)].add(x)
                        stand=buersten(stand)
                        if erfuellbar(stand): 
                            return True
                        stand=old.copy()
                return False


# Sie duerfen diese Funktion veraendern. Kennzeichnen Sie geaenderte Zeilen mit einem Kommentar. Beachten Sie, dass die Funktionen einen int zurueck geben soll, und dass der rekursive Aufruf noch die Funktion erfuellbar aufruft!
def wieviele(stand):
	counter = 0 # ADD
	if len([stand[(i,j)] for i in range(9) for j in range(9) if len(stand[(i,j)])==0])>=1: 
		# return False
		return 0 # CHNG
	elif len([stand[(i,j)] for i in range(9) for j in range(9) if len(stand[(i,j)])==1])==81: 
		# print("Wir haben eine Loesung gefunden")
		# ausgabe(stand)
		# return True
		return 1 # CHNG
	else:
		nonsingletons=[(i,j,stand[(i,j)]) for i in range(9) for j in range(9) if len(stand[(i,j)])>1]
		cmp = lambda a,b: len(a[2])>len(b[2])
		nonsingletons = sortiere(cmp,nonsingletons)
		(i,j,ziffern)=nonsingletons.pop()
		ziffernkopie=ziffern.copy()
		old=stand.copy()
		for x in ziffernkopie:
			stand[(i,j)].clear()
			stand[(i,j)].add(x)
			stand=buersten(stand)
			if erfuellbar(stand):
				# return True
				counter+=1 # ADD
				if counter == 2: # ADD
					return counter # ADD
			stand=old.copy()
		# return False
		return counter # CHNG


# Initialisierungen fuer Sudokus. 
		
# Sie duerfen diese Funktion nicht veraendern.
def init1():
	stand[(0,0)]={8}
	stand[(1,2)]={3}
	stand[(1,3)]={6}
	stand[(2,1)]={7}
	stand[(2,4)]={9}
	stand[(2,6)]={2}
	stand[(3,1)]={5}
	stand[(3,5)]={7}
	stand[(4,4)]={4}
	stand[(4,5)]={5}
	stand[(4,6)]={7}
	stand[(5,3)]={1}
	stand[(5,7)]={3}
	stand[(6,2)]={1}
	stand[(6,7)]={6}
	stand[(6,8)]={8}
	stand[(7,2)]={8}
	stand[(7,3)]={5}
	stand[(7,7)]={1}
	stand[(8,1)]={9}
	stand[(8,6)]={4}

# Sie duerfen diese Funktion nicht veraendern.
def init2():
	#b={(i,j):{} for i in range(9) for j in range(9)}
	stand[(0,1)]={6}
	stand[(0,3)]={1}
	stand[(0,5)]={4}
	stand[(0,7)]={5}
	
	stand[(1,2)]={8}
	stand[(1,3)]={3}
	stand[(1,5)]={5}
	stand[(1,6)]={6}

	stand[(2,0)]={2}
	stand[(2,8)]={1}

	stand[(3,0)]={8}
	stand[(3,3)]={4}
	stand[(3,5)]={7}
	stand[(3,8)]={6}

	stand[(4,2)]={6}
	stand[(4,6)]={3}




	stand[(5,0)]={7}
	stand[(5,3)]={9}
	stand[(5,5)]={1}
	stand[(5,8)]={4}
	
	stand[(6,0)]={5}
	stand[(6,8)]={2}

	stand[(7,2)]={7}
	stand[(7,3)]={2}
	stand[(7,5)]={6}
	stand[(7,6)]={9}

	stand[(8,1)]={4}
	stand[(8,3)]={5}
	stand[(8,5)]={8}
	stand[(8,7)]={7}

# Sie duerfen diese Funktion nicht veraendern.
def init3():
	stand[(0,8)]={4}

	stand[(1,0)]={6}
	stand[(1,2)]={2}

	stand[(2,3)]={3}
	stand[(2,4)]={1}
	stand[(2,5)]={9}

	stand[(3,1)]={1}
	stand[(3,2)]={3}
	stand[(3,4)]={2}

	stand[(4,1)]={9}
	stand[(4,3)]={8}
	stand[(4,6)]={5}

	stand[(5,1)]={7}
	stand[(5,6)]={3}


	stand[(6,0)]={4}
	stand[(6,7)]={6}

	stand[(7,3)]={7}
	stand[(7,5)]={3}
	stand[(7,7)]={9}

	stand[(8,3)]={9}
	stand[(8,5)]={6}
	stand[(8,7)]={8}

# 2+ Lösungen
def init4():
	stand[(4,4)]={1}

# 0 Lösungen
def init5():
	stand[(4,4)]={1}
	stand[(4,5)]={1}

# Aus Sudoku-App
def init6():
	stand[(0,0)]={9}
	stand[(0,1)]={2}
	stand[(1,0)]={5}
	stand[(2,1)]={3}
	stand[(2,2)]={8}

	stand[(1,3)]={8}
	stand[(1,4)]={7}
	stand[(2,4)]={9}
	stand[(2,5)]={1}

	stand[(3,1)]={5}
	stand[(3,2)]={2}
	stand[(4,1)]={9}
	stand[(5,1)]={7}
	stand[(5,2)]={3}

	stand[(3,3)]={9}
	stand[(3,4)]={3}
	stand[(5,4)]={6}
	stand[(5,5)]={4}

	stand[(3,6)]={1}
	stand[(3,7)]={6}
	stand[(4,7)]={3}
	stand[(5,6)]={9}
	stand[(5,7)]={8}

	stand[(6,3)]={4}
	stand[(6,4)]={1}
	stand[(7,4)]={5}
	stand[(7,5)]={3}

	stand[(6,6)]={2}
	stand[(6,7)]={5}
	stand[(7,8)]={1}
	stand[(8,7)]={7}
	stand[(8,8)]={3}

# "Schwerstes Sudoku der Welt" - https://www.oe24.at/welt/Das-ist-das-schwierigste-Sudoku-der-Welt/1597831 (2010)
def init7():
	stand[(0,2)]={5}
	stand[(1,0)]={8}
	stand[(2,1)]={7}

	stand[(0,3)]={3}
	stand[(2,4)]={1}

	stand[(1,7)]={2}
	stand[(2,6)]={5}

	stand[(3,0)]={4}
	stand[(4,1)]={1}
	stand[(5,2)]={3}

	stand[(3,5)]={5}
	stand[(4,4)]={7}
	stand[(5,3)]={2}

	stand[(3,6)]={3}
	stand[(4,8)]={6}
	stand[(5,7)]={8}

	stand[(6,1)]={6}
	stand[(7,2)]={4}

	stand[(6,3)]={5}
	stand[(8,5)]={9}

	stand[(6,8)]={9}
	stand[(7,7)]={3}
	stand[(8,6)]={7}

# Genau 2 Loesungen
def init8():  
	stand[(0,0)]={9}
	stand[(0,2)]={6}
	stand[(0,4)]={7}
	stand[(0,6)]={4}
	stand[(0,8)]={3}

	stand[(1,3)]={4}
	stand[(1,6)]={2}


	stand[(2,1)]={7}
	stand[(2,4)]={2}
	stand[(2,5)]={3}
	stand[(2,7)]={1}

	stand[(3,0)]={5}
	stand[(3,6)]={1}


	stand[(4,1)]={4}
	stand[(4,3)]={2}
	stand[(4,5)]={8}
	stand[(4,7)]={6}


	stand[(5,2)]={3}
	stand[(5,8)]={5}

	stand[(6,1)]={3}
	stand[(6,3)]={7}
	stand[(6,7)]={5}

	stand[(7,2)]={7}
	stand[(7,5)]={5}

	stand[(8,0)]={4}
	stand[(8,2)]={5}
	stand[(8,4)]={1}
	stand[(8,6)]={7}
	stand[(8,8)]={8}

# "Schwerstes Sudoku der Welt" https://www.surfpoeten.de/apps/sudoku/die-schwersten-sudokus-der-welt/ (2018)
# VORSICHT: Es dauert sehr lange!
def init9():
	stand[(0,0)]={5}
	stand[(0,3)]={9}
	stand[(0,6)]={2}

	stand[(1,0)]={4}
	stand[(1,2)]={1}

	stand[(2,7)]={4}

	stand[(3,0)]={6}
	stand[(3,3)]={2}
	stand[(3,5)]={8}

	stand[(4,1)]={8}
	stand[(4,4)]={7}
	stand[(4,7)]={3}

	stand[(5,8)]={1}

	stand[(6,1)]={9}
	stand[(6,6)]={6}

	stand[(7,4)]={3}

	stand[(8,2)]={3}

def init10():  
	stand[(0,0)]={9}
	stand[(0,2)]={6}
	stand[(0,4)]={7}
	stand[(0,6)]={4}
	stand[(0,8)]={3}

	stand[(1,3)]={4}
	stand[(1,6)]={2}


	stand[(2,1)]={7}
	stand[(2,4)]={2}
	stand[(2,5)]={3}
	stand[(2,7)]={1}

	stand[(3,0)]={5}
	stand[(3,6)]={1}


	stand[(4,1)]={4}
	stand[(4,3)]={2}
	stand[(4,5)]={8}
	stand[(4,7)]={6}


	stand[(5,2)]={3}
	stand[(5,8)]={5}

	stand[(6,1)]={3}
	stand[(6,3)]={7}
	stand[(6,7)]={5}

	stand[(7,2)]={7}
	stand[(7,5)]={5}

	stand[(8,0)]={4}
	stand[(8,2)]={5}
	stand[(8,4)]={1}
	stand[(8,6)]={7}
	stand[(8,8)]={8}


stand={(i,j):set(range(1,10)) for i in range(9) for j in range(9)}
print("Wir wollen folgendes Sudoku loesen")

# init1()
# init2()
# init3()

# 2+ Loesungen
# init4()

# 0 Loesungen
# init5()

# Aus Sudoku-App (1 Loesung | Richtig)
# init6()

# Schwerstes Sudoku (Loesung braucht: 933 Sekunden ~ 15 min)
# init9()

# init10()

ausgabe(stand)
print(wieviele(stand))

# Mit Zeitmessung

# t0 = time.process_time() 
# print(wieviele(stand))
# t1 = time.process_time() - t0
# print("Benötigte Zeit ",t1,"Sekunden")