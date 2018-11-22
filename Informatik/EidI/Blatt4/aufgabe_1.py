hilfs_dict = {}

def summiere(x,e):
	"""
	x: intBaum/Tupel
	e: ebene
	"""

def istIntBaum(x):

	# R1: Jeder int ist ein int Baum
	if type(x) == int:
		return True

	# R2: Es muessen genau 3 Elemente in einem Tupel vorkommen
	elif type(x) == tuple and len(x) == 3:

		# R2: wenn das zweite Element im Tupel kein int ist, ist das Tupel kein IntBaum
		if type(x[1]) != int:
			return False

		# R2: wenn beim ersten und letzten Element des Tupels R1 gilt, dann ist es ein IntBaum
		if istIntBaum(x[0]) and istIntBaum(x[2]):
			return True
		else:
			return False
	else:
		return False

t = (81,-7,(111,-16,-26))
s = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
u = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
v = (((1,2,((11,12,13),9,10)),4,5),6,7)

print(istIntBaum(t))
print(istIntBaum(s))
print(istIntBaum(u))
print(istIntBaum(v))



