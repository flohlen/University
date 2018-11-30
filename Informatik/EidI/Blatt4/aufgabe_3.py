# Gruppe 74
# 35408150 Reinbold, Jonas Florian
# 35395821 Hasert, Yannis

port = []

port.append(int(input("Anzahl von 25 Euro-Muenzen: ")))
port.append(int(input("Anzahl von 17 Euro-Muenzen: ")))
port.append(int(input("Anzahl von 11 Euro-Muenzen: ")))
port.append(int(input("Anzahl von 6 Euro-Muenzen: ")))

betrag = int(input("Zu zahlender Betrag: "))

def passend(x):
	"""
	x = betrag
	"""
	if x == 0:
		return True
	elif x < 0:
		return False
	else:
		if x - 25 >= 0:
			div_anz = int((x - (x%25))/25)
			if div_anz <= port[0] and div_anz != 0:
				x -= div_anz*25
				port[0] -= div_anz
				return passend(x)
			else:
				if x - 17 >= 0:
					div_anz = int((x - (x%17))/17)
					if div_anz <= port[1] and div_anz != 0:
						x -= div_anz*17
						port[1] -= div_anz
						return passend(x)
					else:
						if x - 11 >= 0:
							div_anz = int((x - (x%11))/11)
							if div_anz <= port[2] and div_anz != 0:
								x -= div_anz*11
								port[2] -= div_anz
								return passend(x)						
							else:
								if x - 6 >= 0:
									div_anz = int((x - (x%6))/6)
									print(div_anz)
									if div_anz <= port[3] and div_anz != 0:
										x -= div_anz*6
										port[3] -= div_anz
										passend(x)
									else:
										return False


if betrag <= ((25 * port[0]) + (17 * port[1]) + (11 * port[2]) + (6 * port[3])):
	print("Der Betrag koennte bezahlt werden.")

	if passend(betrag):
		print("Der Betrag kann passend bezahlt werden.")
		print(port)
	else:
		print("Der Betrag kann nicht passend bezahlt werden.")
		print(port)
else:
	print("Der Betrag kann nicht bezahlt werden.")