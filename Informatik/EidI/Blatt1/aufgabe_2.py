eingabe_a = int(input("Bitte geben Sie einen Wert fur a an: "))
eingabe_b = int(input("Bitte geben Sie einen Wert fur b an: "))
for i in range(eingabe_a+2):
	if i==0 or i == eingabe_a+1:
		ez = " " + eingabe_b * "-" + " "
		print(ez)
	else:
		ez = "|" + eingabe_b * " " + "|"
		print(ez)