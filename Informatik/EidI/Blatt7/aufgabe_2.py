# Aufgabe 2:
#
# max(L): 
#	die funktion gibt den groessten element bzw. wert in der liste L zurueck (falls L keine elemente mehr hat bzw leer ist, wird 0 zurueckgegeben),
#	dies geschiet dadurch, dass der wert des ersten elements der liste mit dem groesten wert der restlichen liste verglichen wird und der groessere der beiden Werte zurueck gegeben wird.
# 
# 	die funktion ruft sich rekursiv mit der restliste auf um den groessten wert dieser restliste zu finden.
# 	nach x rekusionsaufrufen tritt der basisfall (siehe oben bzw. klammer erster satz),
# 	dass die liste leer ist, da sie jeweils um das erste element gekuerzt wurde ein und in dem Fall wird dem a in der vorletzten rekursion 0 zugewiesen.
#
# 	diese rueckgabe wird mit dem wert des ersten elements der uebergebenen liste vergliechen und der groessere Wert zurueckgegeben, daruch erhaelt die funktion die naechste rueckgabe, und so weiter...
# 	somit arbeitet sich die funktion von hinten nach vorne bis zum ersten funktionsaufruf vor.
#
# maxmult(L):
#	aehliche vorgehensweise wie max(L).
#	die funktion prueft die groesstmoegliche multiplikation mit dem ersten element der liste (L[0]).
#
#	dies geschiet dadurch, dass der wert von L[0] mit dem groessten wert der restlichen liste (der wert wird durch max(L[1:]) ermittelt) multipliziert.
#
#	im anschluss wird geschaut, ob das groesste produkt, welches aus den elementen der restlichen liste resultiert ohne L[0], also das erste element groesser waere.
# 	um dies zu erreichen, ruft sich die funktion wieder selbst, also rekursiv ohne das erste element bzw. L[0] auf.
# 
#	nach x rekusionsaufrufen tritt der basisfall (die funktion kann kein produkt mehr bilden, da durch das aufrufen ohne das erste element weniger als 2 elemente in der liste enthalten sind) auf. 
# 	dadurch wird 0 zurueckgegeben und daher a auf 0 gesetzt,
#	um nun den rueckgabewert der naechsthoeheren rekursionsstufe zu erhalten, erfolgt der vergleich mit b,
#	welches das produkt aus dem durch den aufruf von max() zurueckgegebenen wert, welcher zu diesem zeitpunkt 0 ist und dem wert des ersten elements der liste, also L[0] ist.
#
# 	mit hilfe dieser zurueckgegebenen werte und nach dem vergleichen erhaelt die funktion die naechsten rueckgaben, und so weiter..
# 	somit arbeitet sich die funktion von hinten nach vorne bis zum ersten funktionsaufruf vor.
#
# 	dadurch wird am ende der wert des groesstmoeglichen produkts von zwei elementen der liste ausgegeben.
#
#
# b) Was ist die Laufzeit des Programms, und warum ist das so?
#
#	laufzeit max(L):
#	lineare rekursionstiefe von Len(L)
#	-> O(len(L))
#	
#	laufzeit maxmult(L):
#	rekurionstiefe von len(L)-2, beim xten aufruf dann (len(L)-x)-schritte fuer funktion max()
#	-> O((len(L))^2)

# c)
#  Ihre Loesung:
#
def maxmult_lin(L):
	if len(L) < 2:
		return 0
	ge = 0 # groesstes element
	zge = 0 # zweit groesstes element
	for z in L:
		if z >= ge:
			zge = ge
			ge = z
		elif z > zge:
			zge = z
	return ge*zge

# Nicht veraendern!
if __name__ == '__main__':
# Ihren globalen Testcode koennen Sie hier platzieren:

	print(maxmult_lin([2,6,4]))
	print(maxmult_lin([2,6,8,1,8]))