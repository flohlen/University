def summiere(x,e):
	multi = lambda f,g : f*g
	# R1: Jeder int ist ein int Baum
	if type(x) == int:
		summe += multi(x,e)
		return True

	# R2: Es muessen genau 3 Elemente in einem Tupel vorkommen
	elif type(x) == tuple and len(x) == 3:

		# R2: wenn das zweite Element im Tupel kein int ist, ist das Tupel kein IntBaum
		if type(x[1]) != int:
			return False
		else:
			summe += multi(x[1],e)

		# R2: wenn beim ersten und letzten Element des Tupels R1 gilt, dann ist es ein IntBaum
		if summiere(x[0],e+1) and summiere(x[2],e+1):
			return summe
		else:
			return False
	else:
		return False

t = ((111,-16,-26),81,-7)
s = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
u = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
v = (((1,2,((11,12,13),9,10)),4,5),6,7)

ib = (1,2,3)

print(summiere(t,1))