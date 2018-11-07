eingabe = str(input("Zeichenkette: "))

klammern = 0
nur_klammern = True
richtig_geklammert = True
if len(eingabe) > 0:
	for i in eingabe:
		if i == "(":
			klammern+=1
		elif i == ")":
			klammern-=1
			if klammern < 0:
				richtig_geklammert = False
		else:
			nur_klammern = False
			break
	if not nur_klammern:
		print("Fehlerhafte Eingabe")
	else:
		print("Zeichenkette besteht nur aus Klammern")
		if richtig_geklammert and klammern == 0:
			print("Zeichenkette ist korrekt geklammert")
else:
	print("Keine Zeichenkette eingegeben")