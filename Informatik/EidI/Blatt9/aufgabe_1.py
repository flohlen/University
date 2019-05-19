# Aufgabe 1
#

def rucksack(schaetze,maxgewicht):

	R = [[0] for x in range(maxgewicht+1)]

	print("Go")
	
	for x in range(len(schaetze)):
		
		for y in range(maxgewicht,-1,-1):
			
			if schaetze[x][0] <= y and R[y][0] < R[ y-schaetze[x][0] ][0] + schaetze[x][1]:
				
				R[y] = R[ y-schaetze[x][0] ] + [True]
				R[y][0] += schaetze[x][1]
			
			else:
				
				R[y] += [False]

			print(x,y,R[y][0],schaetze[x][0],schaetze[x][1],R)
	
	return R[int(maxgewicht)][1::]

# Nicht veraendern!
if __name__ == '__main__':

	beispiel1 = [(2,3),(3,4),(5,6)]
	beispiel2 = [(4,10),(3,1),(5,13),(5,5),(7,21)]
	loesung1 = [True, True, False]
	loesung2 = [True, False, True, False, False]
	if rucksack(beispiel1, 5) != loesung1:
		print(f"Ihre Methode funktioniert nicht fuer Beispiel 1 - ist {rucksack(beispiel1, 5)}, soll aber {loesung1} sein.")
	if rucksack(beispiel2, 10) != loesung2:
		print(f"Ihre Methode funktioniert nicht fuer Beispiel 2 - ist {rucksack(beispiel2, 10)}, soll aber {loesung2} sein.")

# Ihren globalen Testcode koennen Sie hier platzieren:
print(rucksack(beispiel1,5))