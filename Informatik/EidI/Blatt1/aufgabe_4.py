eingabe1 = str(input("Bitte geben Sie mehrere Woerter mit Gross- und Kleinbuchstaben ein: "))
print(eingabe1.lower())
eingabe2 = str(input ("Bitte geben Sie ein Vokal ein: "))
for i in eingabe2:
	if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
		print(eingabe1.lower().replace("a",eingabe2).replace("e",eingabe2).replace("i",eingabe2).replace("o",eingabe2).replace("u",eingabe2))
	else: 
		print("Ehrenlose Eingabe")