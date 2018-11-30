# Gruppe 74
# 35408150 Reinbold, Jonas Florian
# 35395821 Hasert, Yannis

def infix(x):
	if type(x) == int:
		return str(x)
	
	if type(x) == tuple and (str(x[1]) == "+" or str(x[1]) == "-" or str(x[1]) == "/" or str(x[1]) == "*"):
		return ("(" + str(infix(x[0])) + str(x[1]) + str(infix(x[2])) + ")")

def prefix(x):
	if type(x) == int:
		return str(x)
	
	if type(x) == tuple and (str(x[1]) == "+" or str(x[1]) == "-" or str(x[1]) == "/" or str(x[1]) == "*"):
		return (str(x[1]) + str(prefix(x[0])) + str(prefix(x[2])))

def postfix(x):
	if type(x) == int:
		return str(x)
	
	if type(x) == tuple and (str(x[1]) == "+" or str(x[1]) == "-" or str(x[1]) == "/" or str(x[1]) == "*"):
		return (str(postfix(x[0])) + str(postfix(x[2])) + str(x[1]))


t = 5
s = ((2, "+", 3), "+", 4)

print("(Praefixnotation)",prefix(t))
print("(Praefixnotation)",prefix(s))

print("(Infixnotation)",infix(t))
print("(Infixnotation)",infix(s))

print("(Postfixnotation)",postfix(t))
print("(Postfixnotation)",postfix(s))