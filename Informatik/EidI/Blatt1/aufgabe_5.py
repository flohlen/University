

eingabe = str(input("Additionsaufgabe: "))

premium = False
premium2 = True
for i in range(len(eingabe)):
	for j in range(10):
		if eingabe[i] == str(j) or eingabe[i] == "+":
			premium = True
			break
	if premium:
		if not ((i == 0 or i == (len(eingabe)-1)) and eingabe[i] == "+"):
			if eingabe[i] == "+" and eingabe[i] == "+":
				premium2 = True
		else:
			print("Falsche Eingabe")
			break
	else:
		print("Falsche Eingabe")
		break
if premium2:
	print("Ergebnis: ",int(eingabe[0:1]) + int(eingabe[2:3]) + int(eingabe[4:5]))



# for i in range(len(eingabe)):
# 	if i == 0 and eingabe[i] == + 

# richtig = False

# for i in range(len(eingabe)):
# 	if not eingabe[i] == "+":
# 		for j in range(10):
# 			if eingabe[i] == str(j):
# 				richtig = True
# 				break
# 			else:
# 				richtig = False
# 	else:

# 		if len(eingabe)-i>2 and eingabe[i+2] == "+":
# 			richtig = True
# 		else:
# 			richtig = False
# if richtig:
# 	print("richtig")
# else:
# 	print("falsch")