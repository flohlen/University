def checkASCII(x):
	"""
	Überprüfung ob Buchstabe x ein ASCII Zeichen ist
	"""
	for char in x:
		if ord(char) > 127:
			return False
	return True

def caesar(x,y):
	"""
	Zeichenkette x um y Stellen nach rechts verschieben
	"""
	w = ""
	for char in x:
		w += chr((ord(char)+y)%128)
	return w

def un_caesar(x,y):
	"""
	Zeichenkette x um y Stellen nach links zurückverschieben
	"""
	w = ""
	for char in x:
		w += chr((ord(char)-y)%128)
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