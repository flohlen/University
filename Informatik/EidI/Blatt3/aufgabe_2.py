# Eingabe der Listen
G=[]
I=[65,88,G]
H=[2,I]
K=[H,3,H,I]
L=[H,H,I,K]

def intSuperliste(l):
	if len(l) == 0:
		return True
	else:
		for x in l:
			if type(x) == list:
				return intSuperliste(x)
			elif type(x) == int:
				if type(l[-1]) == int:
					return True
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
	if intSuperliste(kopie(L)):
		print("Die Kopie ist eine intSuperliste")
else:
	print("L ist keine intSuperliste.")