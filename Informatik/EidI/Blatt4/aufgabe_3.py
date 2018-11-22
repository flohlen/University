port = []

port.append(int(input("Anzahl von 25€-Muenzen: ")))
port.append(int(input("Anzahl von 17€-Muenzen: ")))
port.append(int(input("Anzahl von 11€-Muenzen: ")))
port.append(int(input("Anzahl von 6€-Muenzen: ")))

betrag = int(input("Zu zahlender Betrag: "))

zr = lambda x,y: x*y

if betrag <= (zr(25,port[0])+zr(17,port[1])+zr(11,port[2])+zr(6,port[3])):
	print("Der Betrag koennte bezahlt werden.")


else:
	print("Der Betrag kann nicht bezahlt werden.")

def passend(x):
	"""
	x = betrag
	"""


	return True

	return False