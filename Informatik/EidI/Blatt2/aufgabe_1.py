def checkASCII(x):
	"""
	Überprüfung ob Buchstabe x ein ASCII zeichen ist
	"""
	for z in x:
		if ord(z) >= 0 and ord(z) <=127:
			return True
	return False

def caesar(x,y):
	"""
	Zeichenkette x um y Stellen nach rechts verschieben
	"""
	w = ""
	for z in x:
		w = w + chr((ord(z)+y)%127)
	return w

def un_caesar(x,y):
	"""
	Zeichenkette x um y Stellen nach links zurückverschieben
	"""
	w = ""
	for z in x:
		w = w + chr((ord(z)-y)%127)
	return w

while True:
	eingabe = str(input("Zeichenkette: "))
	if checkASCII(eingabe):
		schluessel = int(input("Schluessel (natuerliche Zahl): "))
		zve = (input("Zeichenkette verschluesseln (v) oder entschluesseln (e)? ")).lower()
		if zve == "v":
			print(caesar(eingabe,schluessel))
			break
		elif zve == "e":
			print(un_caesar(eingabe,schluessel))
			break
		else:
			print("Eingabe nicht erkannt.")
	else:
		print("Fehlerhafte Zeichenkette.")