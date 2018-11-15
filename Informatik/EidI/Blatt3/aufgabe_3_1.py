cool = 34.5

def baum(x):
	print("x",x)
	if x-34 <= 0 and (x-11)/2 <= 0:
		return x
	else:
		print("Baum A:",x-34)
		print("Baum B:",(x-11)/2)
		if x-34 > 0 and (x-11)/2 > 0:
			if baum(x-34) > baum((x-11)/2):
				return baum((x-11)/2)
			elif baum(x-34) < baum((x-11)/2):
				return baum((x-11)/2)
			else:
				print("Gleich")
				return baum(x-34)


print(baum(34.5))