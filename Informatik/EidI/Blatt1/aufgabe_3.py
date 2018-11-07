anzahl_a=0
anzahl_b=0
anzahl_c=0
anzahl_d=0
richtig=True
eingabe = str(input("Zeichenkette: "))
for i in eingabe:
	if i == "a":
		anzahl_a+=1
	elif i == "b":
		anzahl_b+=1
	elif i == "c":
		anzahl_c+=1
	elif i == "d":
		anzahl_d+=1
	else:
		richtig=False
		print("Fehlerhafte Eingabe")
		break
if richtig:
	print("Anzahl a: ",anzahl_a)
	print("Anzahl b: ",anzahl_b)
	print("Anzahl c: ",anzahl_c)
	print("Anzahl d: ",anzahl_d)