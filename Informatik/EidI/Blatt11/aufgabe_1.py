# 
# Aufgabe 1
#

class Vliste(object):

	def __init__(self,eintrag,nachfolger):
		self.eintrag = eintrag
		self.nachfolger = nachfolger

	def gleich(self,other):
		if self.eintrag != other.eintrag:
			return False

		if self.nachfolger == None and other.nachfolger == None:
			return True

		if self.nachfolger == None or other.nachfolger == None:
			return False

		return self.nachfolger.gleich(other.nachfolger) 

	def append(self,value):
		if self.nachfolger == None:
			self.nachfolger = Vliste(value,None)
			return None

		self.nachfolger.append(value)

		# appl = self
		# while (appl.nachfolger != None):
		# 	appl = appl.nachfolger
		# appl.nachfolger = Vliste(value,None)

	def extend(self,liste):
		if self.nachfolger == None:
			self.nachfolger = liste
			return None

		self.nachfolger.extend(liste)

	def filter(self,func):
		L = []
		while True:
			if func(self.eintrag):
				L.append(self.eintrag)
			if self.nachfolger == None:
				break
			self = self.nachfolger
		return nachVListe(L)

	def map(self,func):
		L = []
		while True:
			L.append(func(self.eintrag))
			if self.nachfolger == None:
				break
			self = self.nachfolger
		return nachVListe(L)

	def nachListe(self):
		L = []
		while True:
			L.append(self.eintrag)
			if self.nachfolger == None:
				break
			self = self.nachfolger
		return L

	def istzirkulaer(self):
		wb = []
		return self.istzirkulaer_h(wb)

	def istzirkulaer_h(self,wb):

		if self.nachfolger == None:
			return False

		if self.nachfolger in wb:
			return True

		wb.append(self)

		return self.nachfolger.istzirkulaer_h(wb)		

def nachVListe(liste):
	if liste == []:
		return None

	L = Vliste(liste[0],None)
	liste.pop(0)
	while liste != []:
		L.append(liste[0])
		liste.pop(0)
	return L


# Nicht veraendern!
if __name__ == '__main__':

	L = Vliste(1, Vliste(2, Vliste(3, None)))


# a)
K = Vliste(5, Vliste("ab", Vliste(0.36, None)))
print("a)",K.nachfolger.nachfolger.eintrag)

# b)

K = Vliste(5, Vliste("ab", Vliste(0.36, None)))
L = Vliste(5, Vliste("ab", Vliste(0.36, None)))
print("b)",K.gleich(L))

# c)

K = Vliste(1, Vliste(2,None))
K.append(3)
L = Vliste(1, Vliste(2, Vliste(3, None)))
print("c)",K.gleich(L))

# d) 
K = Vliste(1, Vliste(2,None))
K.extend(Vliste(3, Vliste(4, None)))
L = Vliste(1, Vliste(2, Vliste(3, Vliste(4, None))))
print("d)",K.gleich(L))

# e)
K = Vliste(1, Vliste(2, Vliste(3,None))).filter(lambda x: x % 2 == 1)
L = Vliste(1, Vliste(3,None))
print("e)",K.gleich(L))

# f)
K = Vliste(1, Vliste(2, Vliste(3,None))).map(lambda x: x + 2)
L = Vliste(3, Vliste(4, Vliste(5,None)))
print("f)",K.gleich(L))

# g)
K = Vliste(1, Vliste(2, Vliste(3,None)))
print("g)",K.nachListe())

# h)
K = nachVListe([1,2,3])
L = Vliste(1, Vliste(2, Vliste(3, None)))
print("h)",K.gleich(L))

# i)
F = Vliste(5, Vliste("ab", Vliste(0.36, Vliste(4, Vliste(5,"ab")))))
F.nachfolger.nachfolger.nachfolger.nachfolger = F
print("i)",F.istzirkulaer())