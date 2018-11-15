def baum(x):

	#print("X:",x,"x-34:",x-34)
	#print("X:",x,"(x-11)/2:",(x-11)/2)

	print("X:",x)
	if x-34 <= 0 and (x-11)/2 <= 0:
		print("Return",x)
		return x
	else:
		print()
		if baum(x-34) < baum((x-11)/2):
			return baum(x-34)
		else:
			return baum((x-11)/2)

eingabe = float(input("Maximale Baumhoehe: "))
print("Der kleinste Baum ist", baum(eingabe), "gross.")