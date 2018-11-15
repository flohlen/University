# Eingabe der Listen
H=[2]
L=[1,H]

def intSuperliste(l):
	if len(l) == 0:
		return True
	else:
		for x in l:
			if type(x) == int:
				return True
			elif type(x) == list:
				intSuperliste(x)
			else:
				return False

def kopie(l):
	SL = []
	for x in l:
		if type(x) == int:
			SL.append(x)
		elif type(x) == list:
			SL.append(kopie(x))
		else:
			return "Fehler!"
	return SL

if intSuperliste(L):
	print(kopie(L))
	if kopie(L):
		print("Die Kopie ist eine intSuperliste")
else:
	print("L ist keine intSuperliste.")