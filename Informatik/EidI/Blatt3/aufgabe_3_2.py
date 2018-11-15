def baum(x):
	print("X1:",x)

	a = x-34
	b = (x-11)/2

	print("A:",a)
	print("B:",b)

	if a > 0 and b > 0:
		baum(a)
		baum(b)
	else:
		return x

baum(34.5)
eingabe = float(input("Maximale Baumhoehe: "))
print("Der kleinste Baum ist", baum(eingabe), "gross.")