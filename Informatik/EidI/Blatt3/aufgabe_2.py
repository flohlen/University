# Eingabe der Listen
H = [5,6,7]
K = [4,H]
L = [1,K,H]

def intSuperliste(l):
	if len(l) == 0:
		return True
	else:
		for x in l:
			if type(l[-1]) == int:
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
	print(intSuperliste(kopie(L)))
else:
	print("L ist keine Superliste.")