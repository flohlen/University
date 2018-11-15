def baum(x):
	if baum_regel_1(x) > baum_regel_2(x):
		return baum_regel_2(x)
	else:
		return baum_regel_1(x)

def baum_regel_1(x):
	if x-34 > 0:
		x = x-34
		if baum_regel_1(x) > baum_regel_2(x):
			return baum_regel_2(x)
		else:
			return baum_regel_1(x)
	else:
		return x

def baum_regel_2(x):
	if (x-11)/2 > 0:
		x = (x-11)/2
		if baum_regel_1(x) > baum_regel_2(x):
			return baum_regel_2(x)
		else:
			return baum_regel_1(x)
	else:
		return x

eingabe = float(input("Baumhöhe:"))
print("Wenn der groesste Baum",eingabe,"ist, dass ist der kleine Baum",baum(eingabe))