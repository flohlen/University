# Gruppe 74
# 35408150 Reinbold, Jonas Florian
# 35395821 Hasert, Yannis


def summiere(x):
	e = 1
	return rechne(x,e)

def rechne(x,e):
	if type(x) == int:
		return x*e
	
	if type(x) == tuple and type(x[1]) == int:
		return (rechne(x[0],e+1) + x[1]*e + rechne(x[2],e+1))


t = ((3,5,-26),4,((3,3,2),1,((-12,9,120),-11,7)))
s = ((111,-16,-26),81,-7)

print(summiere(t))
print(summiere(s))