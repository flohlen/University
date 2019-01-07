# Aufgabe 3:
#
# a)

def hat_schlaufe(buch, i):

	if buch[i] == i:
		return True
	else:
		return False

#
# Welche Laufzeit hat Ihre Funktion, und warum?
#
#	linare laufzeit
#	-> O(n) = O(n)*O(1)
#	
#	ein vergleich von einem woerterbucheintrag (O(n)) mit einem wert (O(1)).
#

# b)

def laenge(buch, i):
	l = 1
	while not hat_schlaufe(buch,i):
		l+=1
		i = buch[i]

	return l


#
# Welche Laufzeit hat Ihre Funktion, und warum?
#
#	exponentielle laufzeit
#	-> O(n^2) = O(n-1)*(O(n)+O(n))
#	
#	im worst-case ist der wert des schluessels der name des naechsten schluessels im woerterbuch.
#	da es kein lasso bzw ring verhalten gibt, wird die while-schleife abgebrochen wenn der (n-1)te schluessel erreicht wird.
#	s1->s2->s3->s4->...->sn-1
#	
#	die zuweisung eines woerterbuchwerts mit der laufzeit O(n) und der aufruf der funktion hat_schlaufe() mit der laufzeit O(n) werden somit (n-1) mal aufgerufen
#

# c)

def eintrag(buch, i, j):

	l = laenge(buch,i)
	if j >= l:
		return -1

	pos = 0
	while not hat_schlaufe(buch,i):
		pos+=1
		if pos == j:
			return buch[i]
		i = buch[i]
	return -1

#
# Welche Laufzeit hat Ihre Funktion, und warum?
#	
#	exponentielle laufzeit
#	-> O(n^4-n^3+n^2) = O(n^2)*(O(n-1)+O(n))*O(n-1)
#
#	ein zugriff auf die funktion laenge mit der laufzeit O(n^2)
#	while-schleife O(n-1) ueber hat_schlaufe() O(n) mit woerterbuchzuweisung O(n-1), da an letzter position die if-abfrage abbricht und keine zuweisung mehr stattfindet
#

# d)

def verlaengere(buch, i, j):

	l = laenge(buch,i)
	for pos in range(l):
		if buch[i] == j:
			return False
		i = buch[i]
		if pos == l-1:
			buch[i] = j
	return True

#
# Welche Laufzeit hat Ihre Funktion, und warum?
#
#	exponentielle laufzeit
#	-> O(n^4+n) = O(n^2)*O(n)*O(n)+O(n)
#
#	ein zugriff auf die funktion laenge mit der laufzeit O(n^2)
#	mit for-schleife ueber den bereich von 0 bis laenge-1 iterieren: O(n)
#	
#	im worst-case ist der wert des schluessels der name des naechsten schluessels im woerterbuch: O(n)
#	s1->s2->s3->s4->...->sn
#
#	wenn im letzten schleifen durchlauf sind und j noch nicht aufgetaucht ist, weisen wir dem letzten knoten den knoten j zu: O(n)
#

# e)

def disjunkt(buch, i, j):
    z = i
    while not hat_schlaufe(buch,z):
        z = buch[z]
    i = z
    z = j
    while not hat_schlaufe(buch,z):
        z = buch[z]
    j = z
    return i != j	

#
# Welche Laufzeit hat Ihre Funktion, und warum?
#
#	exponentielle laufzeit
#	-> O(n^2-n) = 2*O(n-1)*O(n)
#
#	2 mal while-schleife O(n-1) mit woerterbuch zuweisung O(n) 
#


# Nicht veraendern!
if __name__ == '__main__':
# Ihren globalen Testcode koennen Sie hier platzieren:
	
	buch = {0:0,1:3,2:2,3:4,4:4,5:2,6:8,7:6,8:8}


	for char in buch:
		print(hat_schlaufe(buch,char))
	
	print("-"*30)

	for char in range(len(buch)):
		print(laenge(buch,char))

	print("-"*30)

	print(eintrag(buch, 1, 1))
	print(eintrag(buch, 5, 2))

	print("-"*30)

	#print(verlaengere(buch,7,4))
	print(buch)

	print("-"*30)

	print(disjunkt(buch, 6, 7))
	print(disjunkt(buch, 5, 8))